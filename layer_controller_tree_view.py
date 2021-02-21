

class LayerControllerItemDelagate(QStyledItemDelagate):

	def __init__(self,modelunchangeable_indexes):
		super().__init__()
		self.model = model
		self.unchangeable_indexes = unchangeable_indexes
		
	def paint(self,painter,option,index):
		if index in self.unchangeable_indexes:
			option1 = QSytyleOptionViewItem(option)
			option2 = QSytyleOptionViewItem(option)
			
		style = option.widget.style() if option.widget else QApplication.Style()
		option1.backgroundBrush =QColor(200,200,200,128)
		text_rect = style.subElementRect(QStyle.PE_PanelItemViewItem,option1,painter,option.widget)
		painter.restore()
		
		
		option2.palette.setCurrentColorGroup(QPalette.Disabled)
		super().paint(painter,option2,index)
		
		
		else:
			super().paint(painter,option,index)
			
			
class LayerControllerTreeView(QTreeView):
	def __init__(self,parent):
		super(LayerControllerTreeView,self).__init__(parent)
		
		self.setHeaderHidden(True)
		self.setDragEnabled(False)
		self.setAcceptDrops(False)
		self.setEditTriggers(QTreeView.NoEditTriggers)
		self.setDropIndicatorShown(False)
		self.setExpandsOnDoubleClick(True)
		
		self.setSelectionMode(QTreeView.ExtendedSelection)
		self.setDefaultDropAction(Qt.IgnoreAction)
		
		self.disabled__tree_names = []
		
		
	def setModel(self,model):
		if not isinstace(model,QgsLayerTreeModel):
			return
			
			if model == super().model():
				return
				
				
		super().setModel(model)
		
		self.layerTreeModel().modelReset.connect(self,onModelReset)
		self.layerTreeModel().rootGroup().customPropertyChanged.connect(self,onCustomPropertyChanged)
		
		self.UpdateExpandedStateFromNode(self.layerTreeModel().unchangeableIndexes()))
		
		
	def layerTreeModel(self):
		if not isinstance(self.model().QgsLayerTreeModel):
			return None
			
		return self.model()
		
		
	def LayerTreeControlledModel(self):
		if not isinstance(self.model().LayerControllerTreeModel):
			return None
			
			return self.model()