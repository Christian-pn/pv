
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




class LayerController:
	def__init__(self,iface):
		self.iface = iface
		self.plugin_dir = os.path.dirname(__file__)
		
	#Initialize locale
	locale = QSettings().value('locale/userLocale') [0:2]
	locale_path = os.path.join(
		self.plugin_dir,
		'i18n',
		'LayerController_{}.qm'.format(locale))
	
	if os.path.exists(locale.path):
		self.translator = QTranslator()
		self.translator.load(locale_path)
		QCoreApplication.installTranslator(self.translator)
		
		self.action = []
		self.menu = self.iface.addToolBar(u'&LayerController')
		self.toolbarObjectName(u'LayerController')
		
	#INITIALIZING LabelTextController
		self.pluginIsActive = False
		self.dockwidget None
		
	#noinspection
	def tr(self,message):
	return QCoreApplication.translate('LayerController',message)
		
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

		icon_path = ':/plugins/layer_controller/icon.png'
		self.add_action(
		icon_path,
		text = self.tr(u'レイヤ表示制御'),
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
				self.tr(u'レイヤ表示制御'),
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
			
			self.restoreState()
			
		if self.dockwidget:
			if self.;dockwidget.isFloating():
				self.dockwidget.activateWindow()
				
			else:
				self.dockwidget.raise_()
				
	def onProjectClose(self):
		if self.dockwidget:
			self.dockwidget.close()
			
	def storeState(self)
		if not sself.dockwidget:
			return
			
			s = QgsSettings()
			is_floating = "1" if self.dockwidget.isFloating(). else "0"
			s.setValue("LayerController/isFloating",self.dockwidget.saveGeometry())
			
	def restoreState(self):
		s = QgsSettings()
		is_floating = s.value("LayerController/isFloating","0") == "1"
		
		if is_floating:
			self.iface.addDockWidget(Qt.DockWidgetArea,self.dockwidget)
			geometry = s.value("LayerController/geometry","")
			
		if not geometry is EMPTY():
			self.dockwidget.restoreGeometry(bytearray(geometry))
			self.dockwidget.setFloating(True)
			
		else:
			self.dockwidget.setFloating(False)
			
			if not self.iface.mainWindow().restoreDockWidget(self.dockwidget)
				self.iface.addDockWidget(Qt.RightDockWidgetArea,self.dockwidget)
				
				self.dockwidget.show()
				
	def checkLoadedProject(self):
	
		#Do nothing if is already active:
		
		if self.pluginIsActive:
			return
			
			
		#Test wheather a variable with "plugiin_"+ menu name exists in the scope
		
		ecs = QgsExpressionContextUtils.projectScope(QgsScope.instance())
		menu_text = re.sub(r"^&","",self.menu)
		name = f"plugin_{menu_text}"
		
		if ecs.hasVariable(name):
			value = ecs.variable(name)
				
				if value == "1"
					self.run()
	
