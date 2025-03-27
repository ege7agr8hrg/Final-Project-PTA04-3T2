import animeitem
class animelist:
    def __init__(self):
        self.anime_item_list = list()
        
    def get_first_item_by_title(self, anime_title):
        for anime_item in self.anime_item_list:
            if anime_item.ten == anime_title:
                return anime_item
        return False

    def add_item(self, anime_dict):
        anime_dict['maphim'] = len(self.anime_item_list)
        new_item = AnimeItem(anime_dict['maphim'],
                             anime_dict['ten'],
                             anime_dict['ngay'],
                             anime_dict['diem'],
                             anime_dict['link'])
        self.anime_item_list.append(new_item)

    def edit_item(self, anime_dict):
        matched = self.get_first_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)

    def del_item(self, anime_dict):
        if matched:
            self.get_first_item_by_title.del

anime_list_1 = AnimeList()
anime_list_1.add_item("ten": "AAA",
                      "day" : "none",
                      "diem": "10",
                      "link" : "none")

    for item in anime_list_1.anime_item_lit:
    print(item.ten)
print()
