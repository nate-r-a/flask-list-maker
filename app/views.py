from flask import render_template, request, flash, redirect, url_for
from app import app
from Adafruit_Thermal import *
import textwrap

printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout = 5)

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
      if v: print(v)
      if v: printer.println(textwrap.fill(v,32))
  print("testing print list")
  flash('List created')
  return redirect(url_for("list"))
