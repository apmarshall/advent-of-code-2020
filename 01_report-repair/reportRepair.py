def reportRepair(list):
  sorted = list.sort()

  if len(sorted) == 0:
      return NaN
  else:
      t = 2020 - sorted[0]
      if sorted[-1] == t:
          return sorted[0] * sorted[-1]
      elif sorted[-1] > t:
          reportRepair(sorted[:-2])
      else:
          reportRepair(sorted[1:])

