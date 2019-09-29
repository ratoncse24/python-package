class Grade():

	def __init__(self, sub_code, sub_mark, student_mark):
		self.sub_code = sub_code
		self.sub_mark = sub_mark
		self.student_mark = setudent_mark

	def get_grade(self):
		persentae = self._mark_persentage
		if persentae >= 80:
			return 'A+'
		elif persentae >= 70:
			return "A"
		elif persentae >= 60:
			return "B"
		else:
			return "Fail"
		
			
	
	def _mark_persentage(self):
		return ( self.student_mark / self.sub_mark ) * 100