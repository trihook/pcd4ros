import open3d as o3d
import numpy as np
from sklearn.cluster import KMeans
import cv2
import os


def imgs2pcd(rgb, depth, f, c):
    """
    读取彩色图和深度图转为 pcd
    :param rgb:
    :param depth:
    :return:
    """
    color_raw = o3d.io.read_image(rgb)
    depth_raw = o3d.io.read_image(depth)

    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw,
                                                                    convert_rgb_to_intensity=False)
    # 获取图像尺寸
    img = cv2.imread(rgb)
    h, w, _ = img.shape

    # 相机内参
    inter = o3d.camera.PinholeCameraIntrinsic()
    inter.set_intrinsics(w, h, f[0], f[1], c[0], c[1])

    pcd = o3d.geometry.PointCloud().create_from_rgbd_image(rgbd_image, inter)
    return pcd


if __name__ == '__main__':
    PJ_ABS_PATH = os.path.split(os.path.realpath(__file__))[0]
    rgb = os.path.join(PJ_ABS_PATH, "resource", "0001.jpg")
    depth = os.path.join(PJ_ABS_PATH, "resource", "0001.png")
    pcd = imgs2pcd(rgb, depth, [1124, 1134], [755, 555])
    o3d.visualization.draw([pcd], show_ui=False, raw_mode=True, show_skybox=False)  # 窗口高度
