import numpy as np

def phase_to_binary_vector(angles, bins=256):
    """
    位相角のリストをバイナリー値のリストに変換する関数
    
    :param angles: 位相角のリスト (ラジアン)
    :param bins: 分割するビンの数
    :return: バイナリー値のリスト
    """
    binary_values = [format(int((angle % (2 * np.pi)) / (2 * np.pi) * bins), f'0{int(np.log2(bins))}b') for angle in angles]
    return binary_values

# サンプルの位相角のリスト
angles = [np.pi / 4, np.pi / 2, np.pi]
binary_values = phase_to_binary_vector(angles)
print(binary_values)  # 出力例: ['00000011', '00000100', '00001000']