# -*- coding: utf-8 -*-

from flask import render_template, request, flash, redirect, url_for
from app import app
import pickle
import textwrap

#################
# from Adafruit_Thermal import *
# printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout = 5)
# printer.writeBytes(27, 33, 1)
# printer.boldOn()
#################

def columns(arr):
  lines = [textwrap.wrap(("-" + item), 20) for item in arr]
  lines = [item for sublist in lines for item in sublist]
  left = lines[:len(lines)/2]
  right = lines[len(lines)/2:]
  if "-" not in right[0][0]:
    left.append("  " + right[0])
    right.remove(right[0])

  if len(left) < len(right):
    for x in range(len(right)-len(left)):
      left.append("")
  elif len(right) < len(left):
    for x in range(len(left)-len(right)):
      right.append("")

  left = [item.ljust(21) for item in left]
  for i in range(len(right)):
    if right[i] == "" or right[i][0] != "-":
      right[i] = "  " + right[i]


  columns = []
  for i in range(len(left)):
    columns.append(left[i] + " " + right[i])

  return columns

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
def update():
  r = request.form
  for key in r.keys():
    print(key)
    for item in r.getlist(key):
      print(item)
      list_dict[key].append(item)
  pickle.dump(list_dict, open("app/box_lists.pkl", "wb"))
  flash('List(s) updated')
  return redirect(url_for("lists"))

@app.route("/printlist", methods=["POST"])
def printlist():
  r = request.form
  print(r)
  for key in r.keys():
    print(key)
    for line in columns(r.getlist(key)):
      print(line)


  # f = request.form
  # for key in f.keys():
  #   for item in f.getlist(key):
  #     if item:
  #       print(item)
  #       lines = textwrap.wrap(("- " + item),32)
  #       #for line in lines:
  #         #line = line + " ║".decode("utf-8")
  #         #line.decode("utf-8")
  #       #lines = list(map((lambda x: x+ u" ║"), lines)
  #       for line in lines:
  #         # printer.println(line)
  #         print(line)
  #   #print [v.encode('ascii') for v in f.getlist(k)]
  #   # if f.getlist(k) != ['']: printer.feed(3)
  flash('List created')
  return redirect(url_for("lists"))

@app.route("/printsavedlist", methods=["POST"])
def printsavedlist():
  r = request.form
  print(r)
  for key in r.keys():
    print(key)
    for line in columns(r.getlist(key)):
      print(line)
  flash('List printed')
  return redirect(url_for("lists"))