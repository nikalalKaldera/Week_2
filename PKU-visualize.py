import numpy as np
from matplotlib import pyplot as plt
import os


#plt.ion()
skeleton_path = 'F:/Nikalal/Courses/CSIT999/Visualise/Dataset/PKU-MMD/Skeleton_sorted/Subject_updated_list/sample/'
#skeleton_path = 'F:/Nikalal/Courses/CSIT999/Visualise/Dataset/PKU-MMD/Skeleton_sorted/Subject_updated_list/upto_174/'
save_directory = 'F:/Nikalal/Courses/CSIT999/Visualise/Dataset/PKU-MMD/Skeleton_sorted/Subject_updated_list/out_file/'

arms = np.array([24, 12, 11, 10, 9, 21, 5, 6, 7, 8, 22]) - 1  # arm
rightHand = np.array([12, 25]) - 1  #
leftHand = np.array([8, 23]) - 1  #
legs = np.array([20, 19, 18, 17, 1, 13, 14, 15, 16]) - 1  # leg
body = np.array([4, 3, 21, 2, 1]) - 1  # body

left_leg = np.array([15, 16]) - 1
right_leg = np.array([19, 20]) - 1

def _load_files(file_path, file_name, save_skelxyz=True):
    # read lines
    f = open(file_path, 'r')
    datas = f.readlines()
    f.close()
    #max_body = 2
    njoints = 25
    # print(datas)

    # create a dic and update key val pairs
    # print(len(datas))
    nframe = len(datas)
    bodymat = dict()
    bodymat['file_name'] = file_name
    #print(bodymat['file_name'])
    nbody = 2
    #print(nbody)
    bodymat['nbodys'] = []
    bodymat['njoints'] = njoints

    # prepare data holder
    #for body in range(max_body):
    bodymat['skel_body{}'.format(0)] = np.zeros(shape=(nframe, njoints, 3), dtype=object)
    # print(bodymat['skel_body{}'.format(0)])
    cursor = 0
    for frame in range(nframe):

        bodycount = 1
        # print(bodycount)

        if bodycount == 0:
            continue
            # skip the empty frame
        bodymat['nbodys'].append(bodycount)
        #for body in range(bodycount):
        #cursor += 1
        skel_body = 'skel_body{}'.format(0)
        bodyinfo = datas[cursor][:-1].split(' ')
        #print(bodyinfo)

        # update co-ordinates for joints(25)
        #for joint in range(75):
        #cursor += 1
        jointinfo = np.array(bodyinfo[0:75])
        jointinfo = np.array(list(map(float, jointinfo)))
        #print(jointinfo.shape)
        joint_xyz = np.array(jointinfo.reshape(25, 3))
        #print(jointinfo)
        #jointinfo = np.array(list(map(float, jointinfo)))
        #print('bodymat' , bodymat['skel_body{}'.format(0)].shape)
        #print(joint_xyz[0])
        #print(bodymat[skel_body][frame])
        #joint_xyz = np.vectorize(float(joint_xyz))
        for joint in range(njoints):
            if save_skelxyz:
                #print(joint_xyz[joint])
                #print(bodymat[skel_body][frame])
                #bodymat[skel_body][frame, nframe] = jointinfo[:3]
                bodymat[skel_body][frame][joint] = joint_xyz[joint]
                #print(bodymat[skel_body][frame][joint])
                #print(frame)
                #print(joint)
        #print(bodymat[skel_body])
        cursor += 1
    # prune the abundant bodys
    for each in range(1):
        # identify max no.of bodies
        if each >= max(bodymat['nbodys']):
            if save_skelxyz:
                del bodymat['skel_body{}'.format(each)] # delete abundant bodies
    #print(bodymat)
    return bodymat


def plot_skeleton_3d(vertices):
    os.chdir(os.path.dirname(save_directory))
    print(len(vertices))
    #print(vertices[0, 0])
    # draw the vertices
    for frame in range(len(vertices)):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(vertices[frame, :, 0], vertices[frame, :, 1], vertices[frame, :, 2], c='red', marker='*')
        # print(vertices)
        # join body parts
        plt.plot(vertices[frame, arms, 0], vertices[frame, arms, 1], vertices[frame, arms, 2])
        plt.plot(vertices[frame, rightHand, 0], vertices[frame, rightHand, 1], vertices[frame, rightHand, 2], c='b')
        plt.plot(vertices[frame, leftHand, 0], vertices[frame, leftHand, 1], vertices[frame, leftHand, 2], c='g')
        plt.plot(vertices[frame, body, 0], vertices[frame, body, 1], vertices[frame, body, 2], c='m')
        plt.plot(vertices[frame, legs, 0], vertices[frame, legs, 1], vertices[frame, legs, 2], c='y')
        plt.show()

def read_files(dir_path):
    file = []
    video = []
    for files in os.listdir(dir_path):
        if files.endswith('.txt'):
            file_path = os.path.join(dir_path, files)
            with open(file_path, "r") as notes:
                #print(files)
                datas = _load_files(file_path, files)
                temp_file = datas['file_name']
                #print(temp_file)
                temp_video = datas['skel_body0']
                #print(temp_frame)
                file.append(temp_file)
                video.append(temp_video)
                #print(datas['file_name'])
                # temp_file = datas['file_name']
                # # print(temp_file)
                # temp_frame = datas['skel_body0']
                # file.append(temp_file)
                # frame.append(temp_frame)
    #print(len(frame))
    return file, video
    # return file_content


if __name__ == '__main__':
    dic = {}
    a, b = read_files(skeleton_path)
    #print(a)
    for i in range(len(a)):
        #print(i)
        dic[a[i]] = b[i]
    #print(dic)
    print(dic['S010057-R.txt'])
    # print(a['skel_body0'])
    #plot_skeleton_3d(dic['S010057-R.txt'])
    # for i in range(len(a)):
    #     print(i)
    #     dic[a[i]] = b[i]
    #
    # print(dic)

