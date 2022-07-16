"""zdppy_password_hash.utils.scrypt._salsa - salsa 20/8 core, autogenerated by _gen_salsa.py"""
#=================================================================
# salsa function
#=================================================================

def salsa20(input):
    """apply the salsa20/8 core to the provided input

    :args input: input list containing 16 32-bit integers
    :returns: result list containing 16 32-bit integers
    """

    b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15 = input
    v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15 = \
        b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15

    i = 0
    while i < 4:
        # salsa op 0: [4] ^= ([0]+[12])<<<7
        t = (v0 + v12) & 0xffffffff
        v4 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 1: [8] ^= ([4]+[0])<<<9
        t = (v4 + v0) & 0xffffffff
        v8 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 2: [12] ^= ([8]+[4])<<<13
        t = (v8 + v4) & 0xffffffff
        v12 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 3: [0] ^= ([12]+[8])<<<18
        t = (v12 + v8) & 0xffffffff
        v0 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 4: [9] ^= ([5]+[1])<<<7
        t = (v5 + v1) & 0xffffffff
        v9 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 5: [13] ^= ([9]+[5])<<<9
        t = (v9 + v5) & 0xffffffff
        v13 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 6: [1] ^= ([13]+[9])<<<13
        t = (v13 + v9) & 0xffffffff
        v1 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 7: [5] ^= ([1]+[13])<<<18
        t = (v1 + v13) & 0xffffffff
        v5 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 8: [14] ^= ([10]+[6])<<<7
        t = (v10 + v6) & 0xffffffff
        v14 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 9: [2] ^= ([14]+[10])<<<9
        t = (v14 + v10) & 0xffffffff
        v2 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 10: [6] ^= ([2]+[14])<<<13
        t = (v2 + v14) & 0xffffffff
        v6 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 11: [10] ^= ([6]+[2])<<<18
        t = (v6 + v2) & 0xffffffff
        v10 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 12: [3] ^= ([15]+[11])<<<7
        t = (v15 + v11) & 0xffffffff
        v3 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 13: [7] ^= ([3]+[15])<<<9
        t = (v3 + v15) & 0xffffffff
        v7 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 14: [11] ^= ([7]+[3])<<<13
        t = (v7 + v3) & 0xffffffff
        v11 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 15: [15] ^= ([11]+[7])<<<18
        t = (v11 + v7) & 0xffffffff
        v15 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 16: [1] ^= ([0]+[3])<<<7
        t = (v0 + v3) & 0xffffffff
        v1 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 17: [2] ^= ([1]+[0])<<<9
        t = (v1 + v0) & 0xffffffff
        v2 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 18: [3] ^= ([2]+[1])<<<13
        t = (v2 + v1) & 0xffffffff
        v3 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 19: [0] ^= ([3]+[2])<<<18
        t = (v3 + v2) & 0xffffffff
        v0 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 20: [6] ^= ([5]+[4])<<<7
        t = (v5 + v4) & 0xffffffff
        v6 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 21: [7] ^= ([6]+[5])<<<9
        t = (v6 + v5) & 0xffffffff
        v7 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 22: [4] ^= ([7]+[6])<<<13
        t = (v7 + v6) & 0xffffffff
        v4 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 23: [5] ^= ([4]+[7])<<<18
        t = (v4 + v7) & 0xffffffff
        v5 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 24: [11] ^= ([10]+[9])<<<7
        t = (v10 + v9) & 0xffffffff
        v11 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 25: [8] ^= ([11]+[10])<<<9
        t = (v11 + v10) & 0xffffffff
        v8 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 26: [9] ^= ([8]+[11])<<<13
        t = (v8 + v11) & 0xffffffff
        v9 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 27: [10] ^= ([9]+[8])<<<18
        t = (v9 + v8) & 0xffffffff
        v10 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        # salsa op 28: [12] ^= ([15]+[14])<<<7
        t = (v15 + v14) & 0xffffffff
        v12 ^= ((t & 0x01ffffff) << 7) | (t >> 25)

        # salsa op 29: [13] ^= ([12]+[15])<<<9
        t = (v12 + v15) & 0xffffffff
        v13 ^= ((t & 0x007fffff) << 9) | (t >> 23)

        # salsa op 30: [14] ^= ([13]+[12])<<<13
        t = (v13 + v12) & 0xffffffff
        v14 ^= ((t & 0x0007ffff) << 13) | (t >> 19)

        # salsa op 31: [15] ^= ([14]+[13])<<<18
        t = (v14 + v13) & 0xffffffff
        v15 ^= ((t & 0x00003fff) << 18) | (t >> 14)

        i += 1

    b0 = (b0 + v0) & 0xffffffff
    b1 = (b1 + v1) & 0xffffffff
    b2 = (b2 + v2) & 0xffffffff
    b3 = (b3 + v3) & 0xffffffff
    b4 = (b4 + v4) & 0xffffffff
    b5 = (b5 + v5) & 0xffffffff
    b6 = (b6 + v6) & 0xffffffff
    b7 = (b7 + v7) & 0xffffffff
    b8 = (b8 + v8) & 0xffffffff
    b9 = (b9 + v9) & 0xffffffff
    b10 = (b10 + v10) & 0xffffffff
    b11 = (b11 + v11) & 0xffffffff
    b12 = (b12 + v12) & 0xffffffff
    b13 = (b13 + v13) & 0xffffffff
    b14 = (b14 + v14) & 0xffffffff
    b15 = (b15 + v15) & 0xffffffff

    return b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15

#=================================================================
# eof
#=================================================================
