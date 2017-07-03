# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from app import app
# from Adafruit_Thermal import *
import pickle
import textwrap

# printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout = 5)
# printer.boldOn()
# printer.setSize('L')
f = open("app/box_lists.pkl", "rb")
# global list_dict
list_dict = pickle.load(f)
# s = open("app/box_lists.pkl", "wb")

@app.route("/")

@app.route("/lists")
def lists():

  return render_template("lists.html", 
    title="For making box lists",
    list_dict=list_dict)

@app.route("/update", methods=["POST"])
# def update():
#   try:
#     ###
#   finally:
#     pass

@app.route("/printlist", methods=["POST"])
def printlist():
  f=request.form
  for k in f.keys():
    for v in f.getlist(k):
      if v:
        print(v)
        lines = textwrap.wrap(("- "+v),32)
        #for line in lines:
          #line = line + " ║".decode("utf-8")
          #line.decode("utf-8")
        #lines = list(map((lambda x: x+ u" ║"), lines)
        for line in lines:
          # printer.println(line)
          print(line)
    #print [v.encode('ascii') for v in f.getlist(k)]
    # if f.getlist(k) != ['']: printer.feed(3)
  print("testing print list")
  flash('List created')
  return redirect(url_for("list"))
