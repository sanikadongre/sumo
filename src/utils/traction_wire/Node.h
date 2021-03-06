/****************************************************************************/
// Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
// Copyright (C) 2001-2019 German Aerospace Center (DLR) and others.
// This program and the accompanying materials
// are made available under the terms of the Eclipse Public License v2.0
// which accompanies this distribution, and is available at
// http://www.eclipse.org/legal/epl-v20.html
// SPDX-License-Identifier: EPL-2.0
/****************************************************************************/
/// @file    Node.h
/// @author  Jakub Sevcik (RICE)
/// @author  Jan Prikryl (RICE)
/// @date    2019-12-15
/// @note    based on work 2017 Ahmad Khaled, Ahmad Essam, Omnia Zakaria, Mary Nader
///
// Representation of electric circuit nodes, i.e. wire junctions and connection points.
/****************************************************************************/
#ifndef NODE_H
#define NODE_H

#include <vector>
#include <string>

using namespace std;

class Element;

class Node {

private:
    bool isground;
    bool isremovable;
    string name;        // unique property, each object has distinctive and unique name
    int id;                // a sequential ID number, might be useful when making the equation
    int num_matrixRow;    // number of matrix row during solving the equations
    int num_matrixCol;    // number of matrix column during solving the equations
    double voltage;
    vector<Element*>* elements; // too lazy to implement a linked list
                                // each node is connected to one or more element, an element is a resistor or voltage/current source

public:
    // A constructor, same functionality as "init" functions
    Node(string name, int id);

    // connects an element to the node
    void addElement(Element* element);
    // disconnects an element to the node
    void eraseElement(Element* element);
    // getters and setters
    double getVoltage();
    void setVoltage(double voltage);
    int getNumOfElements();
    // iterates through the vector of the node's elements and returns the first, which is not equal to "element" in the argument of the function
    Element* getAnOtherElement(Element* element);
    string& getName();
    bool isGround();
    bool isRemovable() { return isremovable; };
    void setGround(bool isground);
    int getId();
    void setNumMatrixRow(int num);
    int getNumMatrixRow();
    void setNumMatrixCol(int num);
    int getNumMatrixCol();
    void setId(int id);
    vector<Element*>* getElements();
    void setRemovability(bool isremovable);
};

#endif
