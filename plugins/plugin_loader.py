import importlib
import pkgutil
import functools
from enum import Enum, unique
import os,sys

# log part

PLUGIN_PATH = os.environ.get("PLUGIN_PATH", "").split(":")

QUNATIZE_DATASETS = dict() # include dataset pre-process.
QUANTIZE_OPS = dict()
# QUANTIZE_CALIBRATIONS = dict() 
QUANTIZE_METRIC = dict()
QUANTIZE_PARSERS = dict()
QUANTIZE_POSTPROCESS = dict()


PLUGIN_PREFIX = "Q_"

class PluginTypeError(Exception):
    pass


@unique
class PluginType(Enum):
    Quantize = 0x00
    Dataset  = 0x01
    Metric   = 0x02
    Parser   = 0x03
    Postprocess = 0x04

PLUGINS = {t: dict() for t in PluginType}
VERSIONS = {t:dict() for t in PluginType}

def register_plugin(type, version=0):
    """
    register a plugin with type and version.
    support plugin type: parser, quantize, post_proposs, serialize.
    """
    global PLUGINS, VERSIONS
    def to_float(str_version):
        try:
            fval = float(str_version)
        except:
            split_version = str_version.strip(' ').split(".")
            fval = float('.'.join([split_version[0], ''.join(split_version[1:])]))
        return fval

    def wrapper(cls):
        if type not in PluginType:
            raise PluginTypeError("Unsupported Pligin Type.")
        
        if type == PluginType.Quantize:
            