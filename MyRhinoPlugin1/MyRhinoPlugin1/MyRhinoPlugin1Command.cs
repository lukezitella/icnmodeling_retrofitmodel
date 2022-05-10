using System;
using System.Collections.Generic;
using Rhino;
using Rhino.Commands;
using Rhino.Geometry;
using Rhino.Input;
using Rhino.Input.Custom;




namespace MyRhinoPlugin1
{
    public class MyRhinoPlugin1Command : Command
    {
        public MyRhinoPlugin1Command()
        {
            // Rhino only creates one instance of each command class defined in a
            // plug-in, so it is safe to store a refence in a static property.
            Instance = this;
        }

        ///<summary>The only instance of this command.</summary>
        public static MyRhinoPlugin1Command Instance { get; private set; }

        ///<returns>The command name as it appears on the Rhino command line.</returns>
        public override string EnglishName => "MyRhinoPlugin1Command";

        //returns the planes created by the orthogonal vectors x, y, and z 
        //which can have any non-zero magnitude
        public static Plane[] planes(int x, int y, int z) {
            Point3d corner1 = new Point3d(0, 0, 0);
            Point3d corner2 = new Point3d(x, 0, 0);
            Point3d corner3 = new Point3d(x, y, 0);
            Point3d corner4 = new Point3d(0, y, 0);
            Plane[] planeList = new Plane[4];
            planeList[0] = new Plane(corner1, corner2, new Point3d(x, 0, z));
            planeList[1] = new Plane(corner4, corner3, new Point3d(x, y, z));
            planeList[2] = new Plane(corner1, corner4, new Point3d(0, y, z));
            planeList[3] = new Plane(corner2, corner3, new Point3d(x, y, z));
            return planeList;
        }




        public class DataSet
        {
            Brep[] Rooms;
            Brep[] Windows;
            Brep[] Doors;
            public DataSet(Brep[] rooms, Brep[] windows,Brep[] doors) {
                Rooms = rooms;
                Windows = windows;
                Doors = doors;
            }
        }

        public static Brep MakeFloor(int height, int startingY, int width,int length)
        {
            Point3d pt0= new Point3d(-.5*length, -.5*width, startingY);
            
            Point3d pt1= new Point3d(.5*length, .5*width, startingY+height);
            
            RhinoApp.Write(pt0.ToString());
            RhinoApp.Write(pt1.ToString());
            return Brep.CreateFromBox(new BoundingBox(pt0, pt1));
        }



        protected override Result RunCommand(RhinoDoc doc, RunMode mode)
        {
            // TODO: start here modifying the behaviour of your command.
            // ---
            RhinoApp.WriteLine("The {0} command will add a line right now.", EnglishName);

            Point3d pt0;
            
            

            Point3d pt1;
            pt1=new Point3d(10,10,10);
            pt0 = new Point3d(0, 0, 0);
            
            Point3d win3 = new Point3d(6, 0, 6);
            Point3d win2 = new Point3d(6, 0, 4);
            Point3d win1 = new Point3d(4, 0, 6);
            Point3d win0=new Point3d(4,0, 4);
            
            Point3d door0 = new Point3d(0, 4, 0);

            Point3d door1 = new Point3d(0, 4, 6);
            Point3d door2 = new Point3d(0, 6, 0);
            Point3d door3 = new Point3d(0, 6, 6);


            BoundingBox box1 = new BoundingBox(pt0, pt1);
           
            

            
            




            
            Brep boxbrep = Brep.CreateFromBox(box1);
            

            Polyline door = new Polyline();
            door.Add(door0);
            door.Add(door2);
            PolylineCurve doorcurve = new PolylineCurve(door);
            Surface doorsurface = Surface.CreateExtrusion(doorcurve, new Vector3d(0, 0, 6));
            Brep doorbrep = doorsurface.ToBrep();


            Polyline win=new Polyline();
            win.Add(win0);
            win.Add(win1);
            PolylineCurve windowcurve = new PolylineCurve(win);

            Surface windowsurface = Surface.CreateExtrusion(windowcurve, new Vector3d(2,0,0));
            Brep windowbrep=windowsurface.ToBrep();









            Brep floor1 = MakeFloor(10, 0, 10, 10);
            Brep floor2 = MakeFloor(10, 10, 20, 10);
            Brep floor3=MakeFloor(10, 20, 20, 20);
            Brep floor4=MakeFloor(20, 30, 20, 10);
            doc.Objects.AddBrep(floor1);
            doc.Objects.AddBrep(floor2);
            doc.Objects.AddBrep(floor3);
            doc.Objects.AddBrep(floor4);


            //doc.Objects.AddBrep(boxbrep);
            //doc.Objects.AddBrep(windowbrep);
            //doc.Objects.AddBrep(doorbrep);








            doc.Views.Redraw();
            RhinoApp.WriteLine("The {0} command added one line to the document.", EnglishName);

            // ---
            return Result.Success;
        }
    }
}
