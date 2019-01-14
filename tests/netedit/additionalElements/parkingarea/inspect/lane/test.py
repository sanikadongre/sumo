#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
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

# go to additional mode
netedit.additionalMode()

# select parkingArea
netedit.changeAdditional("parkingArea")

# change reference to center
netedit.modifyAdditionalDefaultValue(10, "reference center")

# create parkingArea in mode "reference center"
netedit.leftClick(referencePosition, 250, 150)

# go to inspect mode
netedit.inspectMode()

# Change parameter lane with a non valid value (dummy lane)
netedit.modifyAttribute(4, "dummy lane")

# Change parameter lane with a valid value (different edge)
netedit.modifyAttribute(4, "gneE0_0")

# Change parameter lane with a valid value (original edge, same lane)
netedit.modifyAttribute(4, "gneE2_1")

# Change parameter lane with a valid value (original edge, different lane)
netedit.modifyAttribute(4, "gneE2_0")

# Check undos and redos
netedit.undo(referencePosition, 3)
netedit.redo(referencePosition, 3)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)