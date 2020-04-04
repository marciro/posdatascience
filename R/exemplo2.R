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
          highway_miles_per_gallon = hwy,
          engine_displacement = displ)

view(mpg2,title = 'dados')

mpg_ <- select(mpg2, year, model, city_miles_per_gallon)
view(mpg_)

mpg2%>%select(year,model,city_miles_per_gallon)%>%
arrange(year)%>%
  View()

mpg2 %>% 
  count(manufacturer,year) %>% 
  arrange(n) %>%
  spread(year,n)%>%
  View()

mpg2 %>%
  group_by(manufacturer,year) %>%
  summarise(
    media_cidade = mean(city_miles_per_gallon),
    media_estrada = mean(highway_miles_per_gallon)
  )%>%
  mutate(diff_media = media_estrada - media_cidade)%>%
  arrange(diff_media)%>%
  filter(media_cidade>20)%>%
  View()


mpg2 %>% ggplot(aes(x=manufacturer)) + geom_bar() + coord_flip()

mpg2 %>% group_by(manufacturer) %>% 
  summarise(media_cidade = mean(city_miles_per_gallon))%>%
  ggplot(aes(x= manufacturer, y=media_cidade)) + geom_bar(stat= "identity") + labs(x="Fabricante",y="Média na cidade",title = "Consumo médio na cidade por fabricante")+coord_flip()


#mpg2 %>% filter(transmission == 4) %>%
#  ggplot(aes(x=transmission)) %>%
mpg2 %>%
  group_by(drive)%>%
  ggplot(aes(city_miles_per_gallon))+
  geom_density(bins=30) +  facet_grid(fuel_type ~ drive)
  #facet_wrap(~drive)

#Facet wrap - Quebra por categoria (quando é tibble é agrupado)



library(modelr)

modelo <- lm(city_miles_per_gallon ~ engine_displacement, mpg2)

modelo$coefficients

mpg2 <- mpg2 %>%
  add_predictions(modelo)

mpg2 %>% 
  ggplot(aes(engine_displacement))+
  geom_point(aes(y=city_miles_per_gallon),color = "red")+
  geom_point(aes(y=pred), color ="green")+
  facet_wrap(~drive)

# Análise residual

mpg2 %>%
  ggplot(aes(city_miles_per_gallon))


