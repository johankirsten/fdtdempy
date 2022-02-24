from fdtdempy.fields import DipoleCurrentField
from fdtdempy.fields import AggregatedField
from fdtdempy.fields import ZeroField
from fdtdempy.fields import StimulatedField
from fdtdempy.core import Dimension
from fdtdempy.core import Simulation

import math

def Experiment():
    dipoleCurrentField = DipoleCurrentField()
    dipoleCurrentField.SetCurrentDirection(1)
    dipoleCurrentField.SetAmplitude(1)
    dipoleCurrentField.SetFrequency(3 * math.pow(10, 9))
    dipoleCurrentField.SetdX(0.001)
    dipoleCurrentField.CenterXIndex = 100
    dipoleCurrentField.CenterYIndex = 27
    dipoleCurrentField.CenterZIndex = 27
    dipoleCurrentField.LengthIndex = 50
    dipoleCurrentField.Orientation = 0

    jx = AggregatedField()
    jx.CalculatedFieldList.append(dipoleCurrentField)

    jy = ZeroField()

    jz = ZeroField()

    ex = StimulatedField()
    ex.Name = "Ex"
    ex.FilePath = "C:\\Temp\\python\\Ex.csv"
    ex.xDimension = Dimension()
    ex.xDimension.Step = 2
    ex.xDimension.Begin = 0
    ex.xDimension.End = 200
    ex.yDimension = Dimension()
    ex.yDimension.Step = 2
    ex.yDimension.Begin = -1
    ex.yDimension.End = 61
    ex.zDimension = Dimension()
    ex.zDimension.Step = 2
    ex.zDimension.Begin = -1
    ex.zDimension.End = 61
    ex.WriteXIndexBegin = 100
    ex.WriteXIndexEnd = 102
    ex.WriteYIndexBegin = 1
    ex.WriteYIndexEnd = 59
    ex.WriteZIndexBegin = 27
    ex.WriteZIndexEnd = 29
    ex.Init()

    ey = StimulatedField()
    ey.Name = "Ey"
    ey.FilePath = "C:\\Temp\\python\\Ey.csv"
    ey.xDimension = Dimension()
    ey.xDimension.Step = 2
    ey.xDimension.Begin = -1
    ey.xDimension.End = 201
    ey.yDimension = Dimension()
    ey.yDimension.Step = 2
    ey.yDimension.Begin = 0
    ey.yDimension.End = 60
    ey.zDimension = Dimension()
    ey.zDimension.Step = 2
    ey.zDimension.Begin = -1
    ey.zDimension.End = 61
    ey.Init()

    ez = StimulatedField()
    ez.Name = "Ez"
    ez.FilePath = "C:\\Temp\\python\\Ez.csv"
    ez.xDimension = Dimension()
    ez.xDimension.Step = 2
    ez.xDimension.Begin = -1
    ez.xDimension.End = 201
    ez.yDimension = Dimension()
    ez.yDimension.Step = 2
    ez.yDimension.Begin = -1
    ez.yDimension.End = 61
    ez.zDimension = Dimension()
    ez.zDimension.Step = 2
    ez.zDimension.Begin = 0
    ez.zDimension.End = 60
    ez.Init()

    hx = StimulatedField()
    hx.Name = "Hx"
    hx.FilePath = "C:\\Temp\\python\\Hx.csv"
    hx.xDimension = Dimension()
    hx.xDimension.Step = 2
    hx.xDimension.Begin = 1
    hx.xDimension.End = 199
    hx.yDimension = Dimension()
    hx.yDimension.Step = 2
    hx.yDimension.Begin = 0
    hx.yDimension.End = 60
    hx.zDimension = Dimension()
    hx.zDimension.Step = 2
    hx.zDimension.Begin = 0
    hx.zDimension.End = 60
    hx.Init()

    hy = StimulatedField()
    hy.Name = "Hy"
    hy.FilePath = "C:\\Temp\\python\\Hy.csv"
    hy.xDimension = Dimension()
    hy.xDimension.Step = 2
    hy.xDimension.Begin = 0
    hy.xDimension.End = 200
    hy.yDimension = Dimension()
    hy.yDimension.Step = 2
    hy.yDimension.Begin = 1
    hy.yDimension.End = 59
    hy.zDimension = Dimension()
    hy.zDimension.Step = 2
    hy.zDimension.Begin = 0
    hy.zDimension.End = 60
    hy.Init()

    hz = StimulatedField()
    hz.Name = "Hz"
    hz.FilePath = "C:\\Temp\\python\\Hz.csv"
    hz.xDimension = Dimension()
    hz.xDimension.Step = 2
    hz.xDimension.Begin = 0
    hz.xDimension.End = 200
    hz.yDimension = Dimension()
    hz.yDimension.Step = 2
    hz.yDimension.Begin = 0
    hz.yDimension.End = 60
    hz.zDimension = Dimension()
    hz.zDimension.Step = 2
    hz.zDimension.Begin = 1
    hz.zDimension.End = 59
    hz.WriteXIndexBegin = 100
    hz.WriteXIndexEnd = 102
    hz.WriteYIndexBegin = 0
    hz.WriteYIndexEnd = 60
    hz.WriteZIndexBegin = 27
    hz.WriteZIndexEnd = 29
    hz.Init()

    simulation = Simulation()
    simulation.TimeSteps = 200
    simulation.Jx = jx
    simulation.Jy = jy
    simulation.Jz = jz
    simulation.Ex = ex
    simulation.Ey = ey
    simulation.Ez = ez
    simulation.Hx = hx
    simulation.Hy = hy
    simulation.Hz = hz

    simulation.Init(0.001)
    simulation.Run()

Experiment()

print("Press any key to continue")
input()




