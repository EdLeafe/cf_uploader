#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dabo
dabo.ui.loadUI("wx")

app = dabo.dApp()

# IMPORTANT! Change app.MainFormClass value to the name
# of the form class that you want to run when your
# application starts up.
app.MainFormClass = dabo.ui.dFormMain

app.start()
