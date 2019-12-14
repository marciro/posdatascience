library(tidyverse)
View(mpg)

mpg2 <- transmute(mpg, manufacturer = manufacturer,
               model = model,
               year = year,
              cylinders = cyl,
              transmission = trans,
          drive = drv,
          fuel_type = fl,
          class = class,
          city_miles_per_gallon = cty,
          highway_miles_per_gallon = hwy)

view(mpg2,title = 'dados')

mpg_ <- select(mpg2, year, model, city_miles_per_gallon)
view(mpg_)

mpg2%>%
  select(year,model,city_miles_per_gallon)
      %>%
  arrange(year)
  %>%
  View()


