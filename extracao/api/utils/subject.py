from ..models import Subject

class SubjectUtils:

  @classmethod
  def get_all(cls):
    return Subject.objects.all()
  
  @classmethod
  def get_by_id(cls, u_id):
    try:
      subject = Subject.objects.get(id=u_id)
      return subject
    except Subject.DoesNotExist:
      return False