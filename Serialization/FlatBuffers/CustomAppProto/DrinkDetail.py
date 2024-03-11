# automatically generated by the FlatBuffers compiler, do not modify

# namespace: CustomAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class DrinkDetail(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DrinkDetail()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDrinkDetail(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # DrinkDetail
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DrinkDetail
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # DrinkDetail
    def Quantity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def DrinkDetailStart(builder): builder.StartObject(2)
def Start(builder):
    return DrinkDetailStart(builder)
def DrinkDetailAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AddName(builder, name):
    return DrinkDetailAddName(builder, name)
def DrinkDetailAddQuantity(builder, quantity): builder.PrependInt32Slot(1, quantity, 0)
def AddQuantity(builder, quantity):
    return DrinkDetailAddQuantity(builder, quantity)
def DrinkDetailEnd(builder): return builder.EndObject()
def End(builder):
    return DrinkDetailEnd(builder)