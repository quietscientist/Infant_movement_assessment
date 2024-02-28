class Skeleton:
    def __init__(self):
        self.colors = [
            [255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], 
            [170, 255, 0], [85, 255, 0], [0, 255, 0], [0, 255, 85], 
            [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], 
            [0, 0, 255], [85, 0, 255], [170, 0, 255], [255, 0, 255], 
            [255, 0, 170], [255, 0, 85], [255, 0, 0]
        ]

        self.limbSeq = [
            [2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [2, 9], [9, 10],
            [10, 11], [2, 12], [12, 13], [13, 14], [2, 1], [1, 15], [15, 17],
            [1, 16], [16, 18], [3, 17], [6, 18]
        ]

        self.feature_list = ['Ankle_medianx','Wrist_medianx','Ankle_mediany','Wrist_mediany',\
        'Ankle_IQRx', 'Wrist_IQRx','Ankle_IQRy', 'Wrist_IQRy',\
        'Knee_mean_angle','Elbow_mean_angle','Knee_stdev_angle', 'Elbow_stdev_angle',\
        'Ankle_meanent', 'Wrist_meanent','Ankle_lrCorr_x', 'Wrist_lrCorr_x',\
        'Knee_entropy_angle', 'Elbow_entropy_angle','Knee_lrCorr_angle', 'Elbow_lrCorr_angle',\
        'Ankle_medianvelx','Wrist_medianvelx','Ankle_medianvely','Wrist_medianvely',\
        'Ankle_IQRvelx','Wrist_IQRvelx','Ankle_IQRvely','Wrist_IQRvely',\
        'Knee_median_vel_angle','Elbow_median_vel_angle','Knee_IQR_vel_angle','Elbow_IQR_vel_angle',\
        'Ankle_IQRaccx','Wrist_IQRaccx','Ankle_IQRaccy','Wrist_IQRaccy',\
        'Knee_IQR_acc_angle','Elbow_IQR_acc_angle']

        self.labels_list = ['Median ankle position, x','Median wrist position, x','Median ankle position, y','Median wrist position, y',\
        'IQR ankle position, x', 'IQR wrist position, x','IQR ankle position, y', 'IQR wrist position, y',\
        'Mean knee angle','Mean elbow angle','Stdev. knee angle','Stdev. elbow angle',\
        'Entropy ankle position', 'Entropy wrist position','Cross-correlation ankle position','Cross-correlation wrist position',\
        'Entropy knee angle','Entropy elbow angle','Cross-correlation knee angle','Cross-correlation elbow angle',\
        'Median ankle velocity, x','Median wrist velocity, x', 'Median ankle velocity, y','Median wrist velocity, y',\
        'IQR ankle velocity, x','IQR wrist velocity, x','IQR ankle velocity, y','IQR wrist velocity, y',
        'Median knee angular velocity', 'Median elbow angular velocity','IQR knee angular velocity','IQR elbow angular velocity',\
        'IQR ankle acceleration, x','IQR wrist acceleration, x','IQR ankle acceleration, y','IQR wrist acceleration, y',\
        'IQR knee angular acceleration','IQR elbow angular acceleration']

        self.labels_list_feature = ['Median position, x (l)','Median position, x (l)','Median position, y (l)','Median position, y (l)',\
        'IQR position, x (l)', 'IQR position, x (l)','IQR position, y (l)', 'IQR position, y (l)',\
        'Mean angle (deg.)','Mean angle (deg.)','Stdev. angle (deg.)','Stdev. angle (deg.)',\
        'Entropy position', 'Entropy position','Cross-correlation position','Cross-correlation position',\
        'Entropy angle','Entropy angle','Cross-correlation angle','Cross-correlation angle',\
        'Median velocity, x (l/s)','Median velocity, x (l/s)', 'Median velocity, y (l/s)','Median velocity, y (l/s)',\
        'IQR velocity, x (l/s)','IQR velocity, x (l/s)','IQR velocity, y (l/s)','IQR velocity, y (l/s)',
        'Median angular velocity (deg./s)', 'Median angular velocity (deg./s)','IQR angular velocity (deg./s)','IQR angular velocity (deg./s)',\
        'IQR acceleration, x (l/s\u00b2)','IQR acceleration, x (l/s\u00b2)','IQR acceleration, y (l/s\u00b2)','IQR acceleration, y (l/s\u00b2)',\
        'IQR angular acceleration (deg./s\u00b2)','IQR angular acceleration (deg./s\u00b2)']

        self.labels_list_feature_2 = ['Med. position, x','Med. position, x','Med. position, y','Med. position, y',\
        'IQR position, x', 'IQR position, x','IQR position, y', 'IQR position, y',\
        'Mean angle','Mean angle','Stdev. angle','Stdev. angle',\
        'Entropy position', 'Entropy position','Cross-correlation position','Cross-correlation position',\
        'Entropy angle','Entropy angle','Cross-correlation angle','Cross-correlation angle',\
        'Med. velocity, x','Med. velocity, x', 'Med. velocity, y','Med. velocity, y',\
        'IQR velocity, x','IQR velocity, x','IQR velocity, y','IQR velocity, y',
        'Med. angular velocity', 'Med. angular velocity','IQR angular velocity','IQR angular velocity',\
        'IQR acceleration, x','IQR acceleration, x','IQR acceleration, y','IQR acceleration, y',\
        'IQR angular acceleration','IQR angular acceleration']

        self.labels_list_feature_3 = ['Med ankle pos x','Med wrist pos x','Med ankle pos y','Med wrist pos y',\
        'IQR ankle pos x', 'IQR wrist pos x','IQR ankle pos y', 'IQR wrist pos y',\
        'Mean knee angle','Mean elbow angle','Stdev knee angle','Stdev elbow angle',\
        'Entropy ankle pos', 'Entropy wrist pos','Cross-corr ankle pos','Cross-corr wrist pos.',\
        'Entropy knee angle','Entropy elbow angle','Cross-corr. knee angle','Cross-corr elbow angle',\
        'Med ankle vel x','Med wrist vel x', 'Med ankle vel y','Med. wrist vel y',\
        'IQR ankle vel x','IQR wrist vel x','IQR ankle vel y','IQR wrist vel y',
        'Med knee angle vel', 'Med elbow angle vel','IQR knee angle vel','IQR elbow angle vel',\
        'IQR ankle accel x','IQR wrist accel x','IQR ankle accel y','IQR wrist accel y',\
        'IQR knee angle accel','IQR elbow angle accel']

        self. feature_list_angle = ['Knee_mean_angle','Elbow_mean_angle','Knee_stdev_angle', 'Elbow_stdev_angle',\
        'Knee_entropy_angle', 'Elbow_entropy_angle','Knee_lrCorr_angle', 'Elbow_lrCorr_angle',\
        'Knee_median_vel_angle','Elbow_median_vel_angle','Knee_IQR_vel_angle','Elbow_IQR_vel_angle',\
        'Knee_IQR_acc_angle','Elbow_IQR_acc_angle']

        self.feature_list_x = ['Ankle_medianx','Wrist_medianx','Ankle_mediany','Wrist_mediany',\
        'Ankle_IQRx', 'Wrist_IQRx','Ankle_IQRy', 'Wrist_IQRy',\
        'Ankle_meanent', 'Wrist_meanent','Ankle_lrCorr_x', 'Wrist_lrCorr_x',\
        'Ankle_medianvelx','Wrist_medianvelx','Ankle_medianvely','Wrist_medianvely',\
        'Ankle_IQRvelx','Wrist_IQRvelx','Ankle_IQRvely','Wrist_IQRvely',\
        'Ankle_IQRaccx','Wrist_IQRaccx','Ankle_IQRaccy','Wrist_IQRaccy']

        self.feature_list_wrists = ['Wrist_medianx','Wrist_mediany','Wrist_IQRx', 'Wrist_IQRy',\
        'Wrist_medianvelx', 'Wrist_medianvely','Wrist_IQRvelx', 'Wrist_IQRvely',\
        'Wrist_IQRaccx', 'Wrist_IQRaccy',\
        'Wrist_lrCorr_x', 'Wrist_meanent']

    def get_colors(self):
        return self.colors

    def get_limb_seq(self):
        return self.limbSeq
    
    def get_feature_list(self):
        return self.feature_list
    
    def get_labels_list(self):
        return self.labels_list
    
    def get_labels_list_feature(self):
        return self.labels_list_feature
    
    def get_labels_list_feature_2(self):
        return self.labels_list_feature_2
    
    def get_labels_list_feature_3(self):
        return self.labels_list_feature_3