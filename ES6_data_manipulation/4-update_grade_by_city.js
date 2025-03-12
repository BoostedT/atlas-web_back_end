export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentGrades = students.filter((student) => student.location === city);
  return studentGrades.map((student) => {
    const studentGrade = newGrades.filter((grade) => grade.studentId === student.id);
    if (studentGrade.length > 0) {
      return { ...student, grade: studentGrade[0].grade };
    }
    return { ...student, grade: 'N/A' };
  });
}
