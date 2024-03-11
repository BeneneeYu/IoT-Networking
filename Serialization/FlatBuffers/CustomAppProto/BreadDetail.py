# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class BreadDetail(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BreadDetail()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBreadDetail(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BreadDetail
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BreadDetail
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # BreadDetail
    def Quantity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def BreadDetailStart(builder): builder.StartObject(2)
def Start(builder):
    return BreadDetailStart(builder)
def BreadDetailAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return BreadDetailAddName(builder, name)
def BreadDetailAddQuantity(builder, quantity): builder.PrependFloat32Slot(1, quantity, 0.0)
def AddQuantity(builder, quantity):
    return BreadDetailAddQuantity(builder, quantity)
def BreadDetailEnd(builder): return builder.EndObject()
def End(builder):
    return BreadDetailEnd(builder)