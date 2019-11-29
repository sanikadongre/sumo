#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# apply zoom
netedit.setZoom("25", "0", "25")

# go to additional mode
netedit.additionalMode()

# select BusStop
netedit.changeElement("busStop")

# create BusStop with default parameters
netedit.leftClick(referencePosition, 275, 250)

# select Access detector
netedit.changeElement("access")

# Create Access detector
netedit.selectAdditionalChild(7, 0)
netedit.leftClick(referencePosition, 50, 200)

# go to inspect mode
netedit.inspectMode()

# inspect Access
netedit.leftClick(referencePosition, 46, 181)

# Change block movement
netedit.modifyBoolAttribute(7, True)

# go to move mode
netedit.moveMode()

# try to move Acces
netedit.moveElement(referencePosition, -160, 165, 100, 165)

# go to inspect mode
netedit.inspectMode()

# inspect Access
netedit.leftClick(referencePosition, 46, 181)

# Change block movement
netedit.modifyBoolAttribute(7, True)

# go to move mode
netedit.moveMode()

# move Acces
netedit.moveElement(referencePosition, -160, 165, 100, 165)

# Check undo redo
netedit.undo(referencePosition, 5)
netedit.redo(referencePosition, 5)

# save additionals
netedit.saveAdditionals(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
