import pandas as pd
import os
from scipy.stats import norm
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
import sys
sys.path.insert(0,'../src/data')
sys.path.insert(0,'../src/modules')
import load_pose_data
import skvideo.io
import itertools
from sklearn.metrics import roc_auc_score, roc_curve
from scipy.linalg import svd

np.float = np.float64
np.int = np.int_


def plot_skel(df, vid, frame,ax,xvar,yvar,limbSeq,colors):
    alpha =.7
    df = df[(df.frame==frame)].reset_index(drop=True)
    for i,limb in enumerate(limbSeq):
        l1 = limb[0]-1; l2 = limb[1]-1;
        if (len(df[df.part_idx==l1])>0) & (len(df[df.part_idx==l2])>0):
            ax.plot([df[df.part_idx==l1][xvar].iloc[0],df[df.part_idx==l2][xvar].iloc[0]], [df[df.part_idx==l1][yvar].iloc[0],df[df.part_idx==l2][yvar].iloc[0]],linewidth=5, color=[j/255 for j in colors[i]], alpha=alpha)
    # plot kp
    for i in range(len(df)):
        ax.plot(df[xvar][i],df[yvar][i], 'o',markersize = 10, color=[j/255 for j in colors[i]], alpha=alpha)

    return
        
def gen_one_frame(df, vid, frame,dpi):
    fig=plt.figure(dpi=dpi)
    canvas = FigureCanvas(fig)
    ax = plt.gca()
    
    plot_skel(df, vid, i, ax, 'x', 'y')
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-3,3)
    ax.set_ylim(-1,2)
    ax.invert_yaxis()
    ax.axis('off')
    canvas.draw()
    width, height = fig.get_size_inches() * fig.get_dpi()
    im = np.fromstring(canvas.tostring_rgb(), dtype='uint8')
    im = im.reshape(int(height), int(width), 3)
    plt.close()
    return im

def get_one_frame(video,f1):
    videogen = skvideo.io.vreader(video)
    new_videogen = itertools.islice(videogen, f1, f1+1, 1)
    for image in new_videogen:
        a = 1
    return image

def normm(df):
    df['Value'] = (df['Value'] - df['Value'].mean())/df['Value'].std()
    return df
