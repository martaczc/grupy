#Projekt modelu ewolucji współpracy między osobnikami w metapopulacji#

*Marta Czarnocka-Cieciura*

##Wstęp##
Termin metapopulacja oznacza populację danego gatunku zamieszkującą nieciągłe środowisko, składające się z płatów odpowiednich do zamieszkania poprzedzielanych obszarem unikanym przez dany gatunek (subpopulacje), ale umożliwiającym przynajmniej sporadyczne przemieszczanie się osobników między dogodnymi terenami. W ten sposób można patrzeć np. na motyle lub drobne ptaki zamieszkujące sąsiadujące ze sobą wyspy, na skorupiaki w kompleksie jezior lub na pasożyty, dla których gospodarze stanowią takie właśnie środowiskowe "wyspy", poprzedzielane niegościnnym środowiskiem zewnętrznym. 

Pierwszy model dynamiki metapopulacji, stworzony przez Levinsa (levins 1969), był bardzo uproszczony: rozważano w nim jedynie proporcję stanowisk zajętych, przy mało realistycznych założeniach, że wszystkich dostępnych płatów siedliska jest nieskończenie wiele, że są one identyczne i że szansa na przemieszczenie się organizmu między dowolnymi dwoma płatami jest równa. Od tego czasu powstało wiele bardziej szczegółowych modelów funkcjonowania metapopulacji, nastawionych na badanie różnych aspektów ekologii i genetyki populacji, popartych badaniami empirycznymi i mających szerokie zastosowanie w ochronie przyrody (Hanski & Simberloff 1997).

Jedną z ciekawych obserwacji wynikających z badań metapopulacji jest wpływ takiego nieciągłego rozmieszczenia osobników na ewolucję przynajmniej niektórych cech danego gatunku. Taki wpływ postuluje się między innymi na skłonności migracyjne: na poziomie lokalnych subpopulacji migracje są niekorzystne ze względu na duże ryzyko śmierci migranta, ale ponieważ kolonista może odnieść ogromny sukces w nowym siedlisku, więc skłonność do migracji utrzymuje się. Podobny wpływ może mieć struktura przestrzenna populacji na ewolucję strategii rozrodczych - rozmnażanie płciowe czy partenogeneza (Olivieri & Gouyon 1997). Celem mojego modelu będzie zbadanie, czy rozmieszczenie organizmów w metapopulacji może wpływać na ewolucję zjawiska współpracy i altruizmu względem osobników tworzących lokalne subpopulacje.

Biologia ewolucyjna tłumaczy zjawisko pomagania innym osobnikom doborem krewniaczym, altruizmem odwzajemnionym lub innymi ukrytymi korzyściami, jakie może odnieść osobnik dający coś innemu. W ten sposób warunkiem koniecznym dla wystąpienia zachowań altruistycznych staje się umiejętność rozpoznawania innych, w szczególności krewnych i "uczciwych współpracowników". Dawne wyobrażenie o działaniu dla dobra gatunku, tłumaczone doborem krewniaczym (przypis) zostały odrzucone, ponieważ jak wiadomo z teorii gier, egoistyczne osobniki odnoszą ogromny sukces w populacji naiwnych altruistów i powinny ją szybko zdominować.

To rozważanie nie uwzględnia jednak przestrzennego rozmieszczenia osobników. W przypadku metapopulacji można sobie wyobrazić odmienną sytuację. Załóżmy, że środowisko życia badanego gatunku składa się z płatów dogodnych do zasiedlenia, ale posiadających ograniczoną pulę zasobów, z których mogą korzystać osobniki. Dla uproszczenia zakładam, że zasoby są odnawialne, niech będą to np. związki odżywcze wytwarzane przez gospodarza dla pasożyta lub dogodna do zasiedlenia powierzchnia kamienia dla glonów. Poszczególne osobniki w subpopulacji mogą zachowywać się w sposób neutralny, czyli oddziaływać na inne osobniki jedynie poprzez zużywanie wspólnych zasobów, mogą innym osobnikom aktywnie szkodzić, np. wydzielając toksyczne substancje, aby pozbyć się konkurencji (z punktu widzenia innych osobników jest to analogiczne do zmniejszenia puli zasobów - mniej osobników może żyć na tym samym obszarze), albo wreszcie współpracować, np. wydzielając do otoczenia enzym rozkładający jakiś związek, który normalnie jest niedostępny dla tych organizmów, natomiast po rozłożeniu mogą z niego korzystać wszystkie osobniki z danej subpopulacji (w ten sposób powiększa się pula dostępnych zasobów).

W sytuacji jednej dużej populacji można się spodziewać, że zachowania egoistyczne będą wygrywać. Natomiast w przypadku metapopulacji subpopulacje (grupy) złożone z altruistów powinny prosperować lepiej, niż te złożone z egoistów, a tym samym generować więcej migrantów, trafiających do innych subpopulacji lub kolonizujących wolne płaty siedliska. Co prawda osobniki egoistyczne bardzo szybko rozpowszechniłyby się w populacji altruistów, ale przy niskim tempie migracji w populacji altruistów może przez dłuższy czas nie pojawić się żaden egoista.

Celem tworzonego przeze mnie modelu jest zbadanie czy i przy jakim poziomie migracji i rozmiarach lokalnych siedlisk możliwe jest utrzymanie się i proporcję strategii altruistycznych w obrębie metapopulacji.

##Metody##

Model piszę w Pythonie na podstawie podręcznika modelowania populacji (Sokół 2009) i COG-ABM (Kurdej et all 2012). Będzie to model agentowy (w literaturze ekologicznej ten typ modeli bywa nazywany również individual based model). Postępy w pisaniu modelu można śledzić tu: https://github.com/martaczc/grupy.

Postanowiłam uznać dostępne płaty środowiska za niezmienne w tym sensie, że w czasie symulacji nie przybywa ich ani nie ubywa, chociaż liczebność populacji w poszczególnych płatach może się zmieniać. Postanowiłam również przyjąć założenie, że wszystkie płaty są identyczne i równoodległe w tym sensie, że szanse przeżycia, rozmnożenia się lub wyemigrowania osobnika między każdymi dwoma płatami nie zależą od żadnych cech płata, oprócz własności zamieszkującej go populacji. Postanowiłam nie modelować bezpośrednio dostępnych w płacie zasobów, a jedynie wpływ populacji na osobniki wchodzące w jej skład. 

Dla uproszczenia modelu, a także by lepiej oddać własności bakterii (które były główną inspiracją dla modelu) przyjęłam, że osobniki będą haploidalne, a także że będą się rozmnażać (przez podział) wydając jednorazowo tylko jednego potomka. "Materiał genetyczny" osobnika będzie zaprogramowany na razie jako zmienna binarna odpowiadająca za to, czy dany osobnik jest altruistą, czy nie. Na razie zamierzam pominąć zjawiska mutacji i rekombinacji. 

To, czy osobnik jest altruistą, będzie się przejawiało w prawdopodobieństwie rozmnożenia się osobnika w danym kroku czasowym, które określiłam wzorem:

![p_div = 1/(1+exp(a_div*N_i+b_div+C+d*H_i))](http://www.sciweavers.org/tex2img.php?eq=%24p_%7Bdiv%7D%3D%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28a_%7Bdiv%7DN_i%2Bb_%7Bdiv%7D%2BC%2BdH_i%29%7D%7D%24&bc=White&fc=Black&im=png&fs=24&ff=modern&edit=0)

Jest to często stosowany w ekologii wzór logistyczny, którego parametry oznaczają odpowiednio:

* N<sub>i</sub> - liczebność i-tej subpopulacji
* a<sub>div</sub> - współczynnik odpowiadający za intensywność konkurencji między osobnikami
* b<sub>div</sub> - dodatkowy parametr pozwalający ustalić prawdopodobieństwo podziału przy braku wpływów innych osobników
* C - koszt altruizmu (jeśli osobnik jest altruistą)
* d - współczynnik związany ze skutecznością pomocy ze strony innych osobników
* H<sub>i</sub> - pomoc ze strony innych osobników, zadana wzorem:

![H_i =(sum_j(g_j))/N_i](http://www.sciweavers.org/tex2img.php?eq=%24H_i%20%3D%5Cfrac%7B%5Csum%5Climits_%7Bj%3D1%7D%5E%7BN_i%7Dg_j%7D%7BN_i%7D%24&bc=White&fc=Black&im=png&fs=24&ff=modern&edit=0)

Gdzie g<sub>j</sub> oznacza wartość genu altruizmu kolejnych osobników w subpopulacji i-tej (1, jeśli j-ty osobnik jest altruistą i 0 w przeciwnym przypadku). Parametry zamierzam ustalić w ten sposób, by prawdopodobieństwo rozrodu było malejącą funkcją liczebności populacji i kosztów altruizmu, natomiast rosnącą funkcją pomocy ze strony innych osobników.

Prawdopodobieństwo śmierci poszczególnych osobników zamierzam ustalić jako stałą (p_death). W ten sposób można oszacować spodziewaną liczebność danej subpopulacji przy określonym udziale altruistów, przyjmując, że jest to taka liczebność, przy której rozrodczość równoważy śmiertelność (wzór). Wzór ten ma sens w sytuacji braku migracji, w przeciwnym przypadku należy go traktować jako pewne przybliżenie.

Zamierzam przyjąć, że prawdopodobieństwo emigracji w pojedynczym kroku czasowym będzie zależne wyłącznie od liczebności populacji macierzystej i będzie zadane wzorem:

![p_mig = 1/(1+exp(a_m*N_i+b_m))](http://www.sciweavers.org/tex2img.php?eq=%24p_%7Bmig%7D%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B-%28a_mN_i%2Bb_m%29%7D%7D%24&bc=White&fc=Black&im=png&fs=24&ff=modern&edit=0)

Gdzie a<sub>m</sub> i b<sub>m</sub> to parametry związane z migracją

Przy czym wybór płata docelowego będzie całkowicie losowy.

Zdarzenia śmierci i rozrodu będą niezależne w danym kroku czasowym, natomiast migranci będą rekrutowani spośród osobników, które przeżyły dany krok czasowy. Dzięki temu śmiertelność migrantów można wliczyć w ogólny poziom śmiertelności i nie rozważać jej już osobno.
	
##Spodziewane wyniki##

Podejrzewam, że pomimo, iż "egoiści" będą mieli przewagę nad altruistami w postaci braku dodatkowych kosztów, to jednak zdominowanie subpopulacji przez egoistów pociągnie za sobą zmniejszenie jej liczebności, a co za tym idzie - mniejszą liczbę migrantów. Dlatego podejrzewam, że w sytuacji, gdy liczebności poszczególnych subpopulacji będą na tyle małe, że spontaniczne wymarcia będą się zdarzały często, to wówczas przewaga altruistów objawi się w postaci wyższego prawdopodobieństwa skolonizowania wolnego płata. W tej sytuacji powinna się utrzymać pewna równowaga pomiędzy liczbą egoistów i altruistów w obrębie całej metapopulacji. 

Spodziewam się, że taka równowaga będzie możliwa jedynie w sytuacji umiarkowanego poziomu migracji. Jeśli migracje będą zachodzić bardzo rzadko, to o ostatecznym udziale altruistów i egoistów zaważą przede wszystkim zdarzenia losowe - wymieranie poszczególnych subpopulacji. W sytuacji bardzo dużego poziomu migracji każdy płat zamieszkały przez altruistów zostanie szybko skolonizowany przez egoistów, co najprawdopodobniej poskutkuje wyeliminowaniem altruistów.

Ciekawe będzie zbadać, jak wysoki poziom migracji jest potrzebny do utrzymania altruizmu oraz jak wynik symulacji będzie zależał od warunków początkowych.

##Dalsze możliwości rozbudowania modelu##

Ciekawym tematem do zbadania wydaje mi się wprowadzenie do modelu zjawiska mutacji, jako dodatkowego po migracji sposobu na pojawienie się odmiennych strategii. Ciekawa byłoby również zmiana altruizmu w cechę ilościową, zmienianą przez kolejne mutacje, jak również wprowadzenie "większego egoizmu" - ujemnej wartości altruizmu, czyli aktywnego szkodzenia innym osobnikom dla własnych korzyści. Dzięki takim zmianom można by obserwować, do jakiego poziomu altruizmu zmierza ewolucja w określonych warunkach.

Kolejnym kierunkiem zmian mogłoby być wprowadzenie wymiany genów, zwłaszcza w formie rozmnażania płciowego, dzięki czemu modelowana populacja bardziej przypominałaby populacje zwierzęce lub roślinne, jak również łatwiej byłoby oddzielić kwestię ewolucji współpracy na poziomie subpopulacji od doboru krewniaczego (szczególnie silnego w populacjach klonalnych).

Wreszcie można tak zmienić model, aby bardziej odpowiadał rzeczywistym sytuacjom, np. współpracy bakterii w obrębie biofilmów.

#Literatura#

* Hanski, I.,Simberloff, D.(1997) "The Metapopulation Approach: Its History, Conceptual Domain and Application to Conservation" in: Hanski, I., M. E. Gulpin (red.), "Metapopulation Biology. Ecology, Genetics and Evolution" Academic Press 
* Kurdej, K., Łukasik M., Maj M., Plewczyński D., Rakowski F. (2012) "Agent Based Modeling of cognitive processes in both populations and single cognitive system" on line: https://github.com/cogcomp/cog-abm
* Levins, R. (1969), "Some demographic and genetic consequences of environmental heterogeneity for biological control", Bulletin of the Entomological Society of America 15: 237–240
* Olivieri, I., Gouyon, P. H. (1997), "Evolution of Migration Rates and Other Traits: The Metapopulation Effect" in: Hanski, I., M. E. Gulpin (red.), "Metapopulation Biology. Ecology, Genetics and Evolution", Academic Press: 293-321
* Sokół, M. 2009. Minipodręcznik programowania populacji, układów populacji, dziedziczenia i ewolucji w języku Pascal dla studentów ekologii i ochrony środowiska.Uniwersytet Warszawski, Wydział Biologii, on line: www.biol.uw.edu.pl/informatyka, Pascal-Minipodręcznik.
