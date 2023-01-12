import csv

class PageMaker:
  template = ''
  movies = []

  def __init__(self, file_path):
    header = True
    with open(file_path, 'r') as f:
      rows = csv.reader(f, delimiter=',')
      for r in rows:
        if not header:
          self.movies.append({
            'year': int(r[0]), 
            'score': int(r[1]), 
            'title': r[2]
          })
        else:
          header = False

  def load_template(self, file_path):
    with open(file_path, "r") as f:
      self.template = f.read()
 
  def generate_html(self, ouput_dir_path):
    for i, movie in enumerate(self.movies):
      page = self.template \
        .replace('[Title]', movie['title']) \
        .replace('[Year]', str(movie['year'])) \
        .replace('[Score]', str(movie['score']))
      
      dst = "{}/page{}.html".format(ouput_dir_path, i+1)
      with open(dst, 'w') as f:
        f.write(page)
        print(f'[+] page {dst} generated')

  def get_movies(self):
    return self.movies

  def get_template(self):
    return self.template

  def build_index_page(self):
    # Pour compléter
    # générer une page d'accueil (index.html)
    # contenant les liens vers chacune des pages de film
    pass


#---------------------------------------
pm = PageMaker('../deniro.csv')
pm.load_template('../template.html')
pm.generate_html('pages')