import os
import gc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.animation as animation
from tqdm import tqdm
import multiprocessing as mp
import cv2
import argparse

INCLUDE_VID = False

colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0],
          [0, 255, 0], \
          [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255],
          [85, 0, 255], \
          [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85],[255, 0, 0]]

limbSeq = [[2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [2, 9], [9, 10], \
           [10, 11], [2, 12], [12, 13], [13, 14], [2, 1], [1, 15], [15, 17], \
           [1, 16], [16, 18], [3, 17], [6, 18]]

def get_all_frames(vid):
    frames = []

    path = vid
    cap = cv2.VideoCapture(path)
    ret = True
    while ret:
        ret, img = cap.read() # read one frame from the 'capture' object; img is (H, W, C)
        
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frames.append(img)
            
    cap.release()
    
    return frames

def main(n_vid, vid_pkl):
    try: 
        print('clearing old garbage')
        del df
        gc.collect()
    except:
        pass

    output_dir = '/workspaces/Infant_movement_assessment/data/coco_pose_estimates/Panda2B_nonorm/animations_nonorm/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Variables to be defined by user
    print('Loading data...')
    #df = pd.read_pickle('/workspaces/Infant_movement_assessment/data/coco_pose_estimates/Panda2B_nonorm/processed_pose_estimates_coords_nonorm.pkl')
    df = pd.read_pickle(vid_pkl)
    #limbSeq = []  # Replace with your limb sequence data
    #colors = []  # Replace with your colors list

    vids = df.video.unique()
    vid = vids[n_vid]
    
    if INCLUDE_VID:
        video_path = f'/workspaces/Infant_movement_assessment/data/videos/{vid}.mp4'
    else:
        video_path = f'{df[df.video == vid].video.iloc[0]}.mp4'

    filename = os.path.join(output_dir, f'nonorm_anim_{os.path.basename(video_path)}')

    if os.path.isfile(filename):
        print(f'Animation for {vid} already exists. Skipping...')
        return

    if INCLUDE_VID:
        print('Gathering frames...')
        all_frames = get_all_frames(video_path)  # Replace with your frames
        n_frames = len(all_frames)
    else:
        print('Skipping frames...')
        all_frames = None
        n_frames = df[df.video == vid].frame.max() + 1

    fps = df[df.video == vid].fps.iloc[0]  # Frames per second
    skel = df.loc[(df.video == vid)].reset_index(drop=True)

    del df
    gc.collect()

    frame_interval = 5  # Interval of frames to use
    dpi = 80  # Dots per inch for saved animation

    alpha = 0.5

    
    print(f'Processing: {vid}')


    fig, ax = plt.subplots()
    ax.axis('off')
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    ax.set_position([0, 0, 1, 1])
    #ax.set_xlim(0, 1280)
    #ax.set_ylim(0, 720)
    ax.invert_yaxis()

    # ims is a list of lists, each row is a list of artists 
    ims = []

    for f in tqdm(range(0, n_frames, frame_interval)):
        frame_skel = skel.loc[(skel.frame == f)].reset_index(drop=True)

        #check if any of x, y is nan
        if any(frame_skel['x'].isna()) or any(frame_skel['y'].isna()):
            #print(f'Frame {f} has NaN values')
            continue

        artists = []

        for i, limb in enumerate(limbSeq):
            l1 = limb[0] - 1
            l2 = limb[1] - 1
            if (len(frame_skel[frame_skel.part_idx == l1]) > 0) & (len(frame_skel[frame_skel.part_idx == l2]) > 0):
                line, = ax.plot([frame_skel[frame_skel.part_idx == l1]['x'].iloc[0], frame_skel[frame_skel.part_idx == l2]['x'].iloc[0]], 
                                [frame_skel[frame_skel.part_idx == l1]['y'].iloc[0], frame_skel[frame_skel.part_idx == l2]['y'].iloc[0]],
                                linewidth=3, color=[j/255 for j in colors[i]], alpha=alpha)
                artists.append(line)

        # plot key points
        try:
            for i in range(18):
                point, = ax.plot(frame_skel['x'][i], frame_skel['y'][i], 'o', markersize=5, color=[j/255 for j in colors[i]], alpha=alpha)
                artists.append(point)
        except KeyError:
                for i in range(17):
                    point, = ax.plot(frame_skel['x'][i], frame_skel['y'][i], 'o', markersize=5, color=[j/255 for j in colors[i]], alpha=alpha)
                    artists.append(point)

        if INCLUDE_VID:            
            im = ax.imshow(all_frames[f], animated=True)
            artists.append(im)
        else:
            im = None

        ims.append(artists)
        plt.close(fig)
        
        del im, artists
        gc.collect()


    ani = animation.ArtistAnimation(fig, ims, interval=int(1/fps*1000*frame_interval), blit=False, repeat_delay=1000)


    print('Saving animation...')
    ani.save(filename, dpi=dpi)
    plt.close('all')

    del ims, fig, ani, ax, all_frames
    gc.collect()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process video and save frames')
    parser.add_argument('--n_vid', type=int, required=True, help='Index of the video to process')
    parser.add_argument('--vid_pkl', type=str, required=True, help='path of the video to process')
    args = parser.parse_args()
    main(args.n_vid, args.vid_pkl)

