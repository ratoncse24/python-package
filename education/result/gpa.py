class Gpa():

	def __init__(self, sub_code, sub_mark, student_mark):
		self.sub_code = sub_code
		self.sub_mark = sub_mark
		self.student_mark = setudent_mark

	def get_gpa(self):
		persentae = self._mark_persentage
		if persentae >= 80:
			return 5.00
		elif persentae >= 70:
			return 4.00
		elif persentae >= 60:
			return 3.00
		else:
			return 0
		
			
	
	def _mark_persentage(self):
		return ( self.student_mark / self.sub_mark ) * 100