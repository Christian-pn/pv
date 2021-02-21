
	#Legend_view.py

import re

from qgis.PyQt.QtCore import QSettings,QTranslator,QCoreApplication,Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction,QDockWidget

from qgis.Core import QgsSettings,QgsMessageLog,QgsProject,QgsExpressionContextUtils

	#Initialize Qt resources from file resources.py

from.resources_rc import*

	#import the code for the dockwidget
from.legend_view_dockwidget import LegendViewDockWidget
import os.path




class LegendView:
	def__init__(self,iface):
		self.iface = iface
		self.plugin_dir = os.path.dirname(__file__)
		
	#Initialize locale
	locale = QSettings().value('locale/userLocale') [0:2]
	locale_path = os.path.join(
		self.plugin_dir,
		'i18n',
		'LegendView_{}.qm'.format(locale))
	
	if os.path.exists(locale.path):
		self.translator = QTranslator()
		self.translator.load(locale_path)
		QCoreApplication.installTranslator(self.translator)
		
		self.action = []
		self.menu = self.iface.addToolBar(u'&LabelTextController')
		self.toolbarObjectName(u'LabelTextController')
		
	#INITIALIZING LabelTextController
		self.pluginIsActive = False
		self.dockwidget None
		
	#noinspection
	def tr(self,message):
	return QCoreApplication.translate('LabelTextController',message)
		
	def add_action(
		self,
		icone_path,
		text,
		callback,
		enable_flag = True,
		add_to_menu = True,
		add_to_toolbar = None,
		status_tip = None,
		whats_this = None,
		parent = None
		):

	icon =QIcon(icon_path)
	action = QAction(icon,text,parent)
	action.triggered.connect(callback)
	action.setEnabled(enabled_flag)

	if status_tip is not None:
		action.setStatusTip(status_tip)
	
	if whats_this is not None:
		action.setWhatsThis(Whats_this)
	
	if add_to_toolbar:
		self.toolbar.addAction(action)
	
	if add_to_menu:
		self.iface.addPluginToMenu(
		self.menu,
		action
		)
	
		self.actions.append(action)
			return action
		
		
	def initGui:

		icon_path = ':/plugins/label_text_controller/icon.png'
		self.add_action(
		icon_path,
		text = self.tr(u'表示テキスト制御'),
		callback =self.run,
		parent = self.iface.mainWindow() 
		)

	#Closing LabelTextController	
	def onClosePlugin(self):
		self.storeState()
	
	#disconnects
		self.dockwidget.closingPluginDisconnect(self.onClosePlugin)
		self.pluginIsActive = False
	
	def unload(self)
		for action in self.actions:
			self.iface.removePluginMenu(
				self.tr(u'表示テキスト制御'),
				self.iface.removeToolBarIcon(action)
		
	#remove toolbar	
				del self.toolbar
				)

	def run(self):
		if not self.pluginIsActive:
			self.pluginIsActive = True;
		
		if self.dockwidget == None:
			self.dockwidget =LabelTextControllerDockWidget(self.iface)
		
	#we add here in Legend_view
			self.dockwidget.setAttribute(Qt.WA_DeleteOnCloce)
	
	#provide cleanup for closing widget
	
			self.dockwidget.closingPlugin.connect(self.onClosingPlugin)
	
	#show the widget
	#allow choice of widget
	
			self.iface.addDockWidget(Qt.RightDockWidgetArea,self.dockwidget)
	
			self.dockwidget.show()
		