# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from app import app
from Adafruit_Thermal import *
import textwrap

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout = 5)
printer.boldOn()
printer.setSize('L')

@app.route("/")

@app.route("/list")
def list():
  return render_template("list.html", 
    title="For making box lists")

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
          printer.println(line)
    #print [v.encode('ascii') for v in f.getlist(k)]
    if f.getlist(k) != ['']: printer.feed(3)
  print("testing print list")
  flash('List created')
  return redirect(url_for("list"))
