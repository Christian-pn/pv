

class LayerControllerTreeModel(QgslayerTreeModel):
	def__init__(self.rootNode:QgsLayerTree,parent:QObject = None):
	super().__init__(rootNode,parent)
	
	#Hide Legend
	super().setFlags(QgsLayerTreeModel.useTextFormatting / QgsLayerTreeModel.AllowNodeChangeVisibility)
	
	super().setAutoCollapseLegendNodes(10)
	
	self.unchangeable_indexes = set()
	
	def setData(sel.index:QModelIndex,value:QVariant,role:int):
		if (role ==Qt.CheckStateRole):
			if ondex in self.unchangeable_indexes:
				return False
				
		return bool(super().setData(index,value,role))
		
	def appendUnchangeableIndex(self,index:QModelIndex):
		self.unchangeable_indexes.add(index)
		
		
	def unchangeableIndexes(self):
		return self.unchangeable_indexes
		
		
	def clearUnchangeableIndexes(self):
		self.unchangeable_indexes.clear()
		