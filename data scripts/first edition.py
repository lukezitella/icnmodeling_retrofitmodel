import Rhino
import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp
import Grasshopper

def create(x,y,z,nWindows, dimWindows):
    corner1 = (0,0,0)
    corner2 = (x,0,0)
    corner3 = (x,y,0)
    corner4 = (0,y,0)
    mid = (x/2,y/2,0)
    cornerZ = (0,0,z)
    vertLineID = rs.AddLine(corner1,cornerZ)
    x_dir = rs.Distance(corner1, corner2)
    y_dir = rs.Distance(corner1, corner4)
    xyplane = rs.WorldXYPlane()
    planarSrf = rs.AddPlaneSurface(xyplane, x_dir, y_dir)
    zone = rs.ExtrudeSurface(planarSrf,vertLineID)
    #zone = Grasshopper.Kernel.Types.GH_ObjectWrapper(zone)
    
    windows = []
    planes = []
    planes.append(rs.PlaneFromPoints((0,0,0),(x,0,0),(x,0,z)))
    planes.append(rs.PlaneFromPoints((0,y,0),(x,y,0),(x,y,z)))
    planes.append(rs.PlaneFromPoints((0,0,0),(0,y,0),(0,y,z)))
    planes.append(rs.PlaneFromPoints((x,0,0),(x,y,0),(x,y,z)))
    rs.AddLayer(name="Windows", color=(255,0,0))
    vert = rs.AddLine((0,0,0),(0,0,dimWindows))

    if nWindows <= 4:
        for i in range(nWindows):
            if i==0:
                line = rs.AddLine((0,0,0),(dimWindows,0,0))
                windows.append(rs.ExtrudeCurve(line, vert))
                rs.MoveObject(windows[i], (x/2 - dimWindows/2, 0, z/2 - dimWindows/2))
                rs.ObjectLayer(windows[i], "Windows")
            elif i == 1:
                line = rs.AddLine((0,0,0),(dimWindows,0,0))
                windows.append(rs.ExtrudeCurve(line, vert))
                rs.MoveObject(windows[i], (x/2 - dimWindows/2, y, z/2 - dimWindows/2))
                rs.ObjectLayer(windows[i], "Windows")
            elif i == 2:
                line = rs.AddLine((0,0,0),(0,dimWindows,0))
                windows.append(rs.ExtrudeCurve(line, vert))
                rs.MoveObject(windows[i], (0, y/2 - dimWindows/2, z/2 - dimWindows/2))
                rs.ObjectLayer(windows[i], "Windows")
            else:
                line = rs.AddLine((0,0,0),(0,dimWindows,0))
                windows.append(rs.ExtrudeCurve(line, vert))
                rs.MoveObject(windows[i], (x, y/2 - dimWindows/2, z/2 - dimWindows/2))
                rs.ObjectLayer(windows[i], "Windows")
    elif nWindows % 2 == 1:
        pass
    elif nWindows%2 == 0:
        pass

def grasshopperAnalyze(zwd, zoneSettings):
    #rs.SelectObject(zwd[0])
    #print(rs.ObjectType(zwd[0]))
    windows = []
    for i in range(len(zwd[1])):
        win = Grasshopper.Kernel.Types.GH_Surface(zwd[1][i])
        windows.append(ghcomp.ClimateStudioGH.CSWindow(win)[0])
    #zoneOut = ghcomp.ClimateStudioGH.CSEnergyZone(zwd[0], "Frame", zoneSettings)
    #print(zoneOut)
    #ghcomp.ClimateStudioGH.RunCSEnergyModel()
    #print(ghcomp.ClimateStudioGH.CSZoneSettings("Frame"))
    print(zwd[0])
    zone = Grasshopper.Kernel.Types.GH_ObjectWrapper(zwd[0])
    print(zone)
    ghcomp.ClimateStudioGH.cs
    zoneOut = ghcomp.ClimateStudioGH.CSEnergyZone(zone, "Frame", zoneSettings)[0]
    print(zoneOut)
    ghcomp.ClimateStudioGH.CSModelMaker(ghcomp.ClimateStudioGH.CSEnergyZone(zone, "Frame", zoneSettings)[0],windows)

building1 = create(25,20,15,3,2)