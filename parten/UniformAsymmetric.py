import numpy as np
import matplotlib.pyplot as plt
# x_f = 3.5

def Asym_singlepoint(x_f):
    Qmax = 255
    Qmin = 0

    x_min = 1000.0
    x_max = 1100.0

    scale = (Qmax - Qmin) / (x_max - x_min)

    zp = round(x_min * scale)
    zp_nuged = np.clip(zp, 0, 255)


    x_q0 = round(x_f*scale - zp)
    x_q1 = round(x_f*scale - zp_nuged)

    x_req0 = (x_q0 + zp) / scale
    x_req1 = (x_q1 + zp_nuged) / scale

    return x_req0, x_req1, x_q0, x_q1

# Asym_singlepoint()

def show_nugeZero_boost():
    GT = []
    no_nuge = []
    with_nuge = []
    # for x in np.arange(1000, 1050, 0.01):
    #     a,b,_,_ = Asym_singlepoint(x)
    #     GT.append(x)
    #     no_nuge.append(a)
    #     with_nuge.append(b)
    # plt.plot(GT, "g--o", label="x_f")
    # plt.plot(no_nuge, "r--o", label="x_req_noZeronuge")
    # plt.plot(with_nuge, "b--o", label="x_req_withZeronuge")
    # plt.legend()
    # plt.show()

    for x in np.arange(1000, 1100, 0.1):
        _,_,a,b = Asym_singlepoint(x)
        GT.append(x)
        no_nuge.append(a)
        with_nuge.append(b)
    plt.plot(no_nuge, "r--o", label="x_req_noZeronuge")
    plt.plot(with_nuge, "b--o", label="x_req_withZeronuge")
    plt.legend()
    plt.show()
    
def Asym_FC(x_f=1050.0, w_f=2.3, b_f=0.9):
    Qmax = 255
    Qmin = 0

    x_min = 1000.0
    x_max = 1100.0

    scale_x = (Qmax - Qmin) / (x_max - x_min)
    zp = round(x_min * scale_x)
    zp_nuged = np.clip(zp, 0, 255)
    x_q = round(x_f*scale_x - zp_nuged)

    scale_w = 127 / 2.5
    w_q = round(w_f * scale_w)

    
    return None




if __name__ == "__main__":
    show_nugeZero_boost()