
class YuGiOhSeries:
  """
  数字与决斗世界名称之间的转换关系
  """

  def __init__(self, name: str, value: int):
    self.name = name
    self.value = value

  @classmethod
  def get_name_by_number(cls, number: int) -> str:
    """
    根据传入的数字，获取到对应的名称
    """
    for series in cls.series_list:
      if series.value == number:
        return series.name
    return None

  @classmethod
  def get_number_by_name(cls, name: str) -> int:
    """
    根据传入的名称，获取到对应的数字
    """
    for series in cls.series_list:
      if series.name == name:
        return series.value
    return None



# 初始化系列列表
YuGiOhSeries.series_list = [
    YuGiOhSeries("DM", 1),
    YuGiOhSeries("DSOD", 2),
    YuGiOhSeries("GX", 3),
    YuGiOhSeries("5Ds", 4),
    YuGiOhSeries("ZEXAL", 5),
    YuGiOhSeries("ARC_V", 6),
    YuGiOhSeries("VRAINS", 7),
    YuGiOhSeries("SEVENS", 8),
]
