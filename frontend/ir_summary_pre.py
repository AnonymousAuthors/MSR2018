
class IRSummaryPre(object):

	@classmethod
	def checkDirtyWords(self,summary):
		import re
		words = []
		SummaryWords = re.split(r'[\s,;.]',summary)
		FileDirty = open('dirty.txt','r')
		filelines = FileDirty.readlines()
		for line in filelines:
			dword = line.split(' ')[0]
			if dword in SummaryWords:
				words.append(dword)
		return words

	@classmethod
	def checkTag(self,summary):
		import re
		tag = []
		if ':' in summary:
			ptag = summary.split(':')[0]
			if len(ptag.split(' ')) == 1:
				tag.append(ptag)
		if summary[0] == '{' and '}' in summary:
			ptag = re.split('{|}',summary)[1]
			tag.append(ptag)
		return tag