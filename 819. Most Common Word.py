class Solution:
  def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    banned = set(banned)
    words = re.findall(r'\w+', paragraph.lower()) # type: ignore
    return collections.Counter( # type: ignore
        word for word in words if word not in banned).most_common(1)[0][0]