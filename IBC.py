import Autodesk
from Autodesk.Revit import DB
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import Transaction

doc = __revit__.ActiveUIDocument.Document

sheets = DB.FilteredElementCollector(doc)\
                   .OfCategory(DB.BuiltInCategory.OST_Sheets)\
                   .WhereElementIsNotElementType()\
                   .ToElements()

ibcsheets = []

for s in sheets:
    param = s.LookupParameter("WM_SHT-Office").AsString()
    if param == "IBC":
        ibcsheets.append(s.Id)

for s in ibcsheets:
    print(s)
print("Test on git")
