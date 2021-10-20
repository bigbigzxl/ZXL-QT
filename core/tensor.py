

class Tensor(object):
    def __init__(self) -> None:
        super().__init__()
        self.name = ""
        self.betensor = None
        self.betensor_type = None
        self.dtype = None
        self.shape = None # -> list
        self.ir_shape= None
        
        self.qbits = None
        self.qinvariant = False
        self.qmax = None
        self.qmin = None

        self.running_histc = None
        self.running_histc_key_axis = None

        self.min = 0.0
        self.min_key_axis = None
        self.max = 0.0
        self.max_key_axis = None
        self.extrema_min = float("-INF")
        self.extrema_min_key_axis = None
        self.extrema_max = float("INF")
        self.extrema_max_key_axis = None
        self.running_min = 0.0
        self.running_min_key_axis = None
        self.running_max = 0.0
        self.running_max_key_axis = None
        self.running_mean = 0.0
        self.running_mean_key_axis = None
        self.running_std = 0.0
        self.running_std_key_axis = None

        self.debug = False
        self.need_deleted = False





