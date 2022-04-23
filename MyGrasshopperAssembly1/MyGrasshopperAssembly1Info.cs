using System;
using System.Drawing;
using Grasshopper;
using Grasshopper.Kernel;

namespace MyGrasshopperAssembly1
{
    public class MyGrasshopperAssembly1Info : GH_AssemblyInfo
    {
        public override string Name => "MyGrasshopperAssembly1";

        //Return a 24x24 pixel bitmap to represent this GHA library.
        public override Bitmap Icon => null;

        //Return a short string describing the purpose of this GHA library.
        public override string Description => "";

        public override Guid Id => new Guid("1EDB13D0-62F9-450E-B970-C95057963116");

        //Return a string identifying you or your company.
        public override string AuthorName => "";

        //Return a string representing your preferred contact details.
        public override string AuthorContact => "";
    }
}