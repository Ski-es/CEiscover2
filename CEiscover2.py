import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie


with st.sidebar:
    selected= option_menu(
        menu_title= 'Table of Contents',
        options= ["Home", "Interesting Fun Facts", "Infrastructure","News and Entertainment", "Contacts"])
    with st.form(key="FORM 1"):
        name = st.text_area(label=" Contact Us If You have Any Concern")
        number = st.text_input("Enter Your Email Address")
        submit = st.form_submit_button(label="Submit this Form")
        print("You have Submitted a Comment, Please wait a Moment for Response")

if selected== "Home":
    st.header('CEiscover: Interesting Fun Facts Lying Under the Cap of a Civil Engineer')
    st.write('Want to know some interesting Facts Lying in Field of Civil Engineering?')


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = ("https://assets3.lottiefiles.com/private_files/lf30_furdejlt.json")
    lottie_json = load_lottieurl(lottie_hello)
    st_lottie(lottie_json)


if selected=="Interesting Fun Facts":
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = ("https://assets2.lottiefiles.com/datafiles/IzfSYsijBrigbf1/data.json")
    lottie_json = load_lottieurl(lottie_hello)
    st_lottie(lottie_json)
    st.write("-------------------------------------------")
    st.title("INTERESTING FACTS IN THE FIELD OF CIVIL ENGINEERING")
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15 = st.tabs(
        ["FACT 1", "FACT 2", "FACT 3", "FACT 4", "FACT 5", "FACT 6", "FACT 7", "FACT 8", "FACT 9", "FACT 10", "FACT 11",
         "FACT 12", "FACT 13", "FACT 14", "FACT 15"])

    with tab1:
        st.subheader("FACT 1")
        st.write(
            "Engineer and architect – one and the same: Until the 18th century, the terms “architect” and “engineer” were interchangeable. They referred to the same person, because the fields of architecture and civil engineering were not yet distinct.")
        st.write(
            "Architects are responsible for the design and planning of structures ranging from houses and factories to skyscrapers and museums, while civil engineers oversee the entire design-to-completion process for buildings, roads, dams, bridges, water systems, and other major works.")


    with tab2:
        st.subheader("FACT 2")
        st.write(
            "Civil engineers – they’ve gone green: Civil engineers do more than design and construct lighthouses. These professionals often assist in planning ways to reduce future pollution and help clean up existing pollution.")
        st.write(
            "Civil engineers work on complex projects, and they can achieve job satisfaction in seeing the project reach completion. Civil engineering is one of the oldest engineering disciplines because it deals with constructed environment including planning, designing, and overseeing construction and maintenance of building structures, and facilities, such as roads, railroads, airports, bridges, harbors, channels, dams, irrigation projects, pipelines, power plants, and water and sewage systems. ")


    with tab3:
        st.subheader("FACT 3")
        st.write(
            "According to payscale, the average civil engineer salary in the Philippines is ₱270,441 a year. Increasing your pay as a Civil Engineer is possible in different ways. Change of employer: Consider a career move to a new employer that is willing to pay higher for your skills. Level of Education: Gaining advanced degrees may allow this role to increase their income potential and qualify for promotions. Managing Experience: If you are a Civil Engineer that oversees more junior Civil Engineers, this experience can increase the likelihood to earn more. ")
        st.write("Base Salary: ₱36k - ₱582k")
        st.write("Bonus: ₱5k - ₱79k")
        st.write("Profit Sharing: ₱5k - ₱280k")
        st.write("Total Pay: ₱107k - ₱888k")

    with tab4:
        st.subheader("FACT 4")
        st.write(
            "Engr. Marcial Kasilag was a 1904 pensionado to the US and a prominent pioneer civil engineer. He was the first registered civil engineer of the Philippines and the father of National Artist for Music Lucrecia Kasilag.")
        st.write(
            "The Philippine Society of Civil Engineers (PSCE) was formed sometime in the late twenties. It was the country’s first civil engineering organization with the late Engr. Marcial Kasilag as its first president. Engr. Marcial Kasilag holds the No.1 slot in the PRC Registry of Civil Engineers. He then occupied a high-ranking position in the government. He was the commissioner for Mindanao and Sulu.")


    with tab5:
        st.subheader("FACT 5")
        st.write(
            "To offer civil engineering services, a professional must have a license. This requirement is consistent across all 50 states. Additionally, you should be at least 21 years old, a Filipino Citizen with good moral character, and must not have been convicted of a crime involving moral turpitude.")
        st.write(
            "Civil engineers need a bachelor’s degree in civil engineering, in one of its specialties, or in civil engineering technology. They typically need a graduate degree and licensure for promotion to senior positions. Although licensure requirements vary by state, civil engineers usually must be licensed if they provide services directly to the public. Retake policies vary by jurisdiction. However, FSBPT will only allow you to take the examination a maximum of three times in any 12-month period.")


    with tab6:
        st.subheader("FACT 6")
        st.write(
            "Construction engineering – executing designs: This sub-discipline of civil engineering involves the execution of designs from engineers involved in structural, hydraulic, transportation and geotechnical projects. Construction engineers manage construction projects, ensuring that they are scheduled and built in accordance with plans and specifications. These engineers typically are responsible for the design and safety of temporary structures used during construction.")
        st.write(
            "A construction engineer can be defined as a civil engineer who is tasked with the oversight and management of a large-scale, complex construction project. Typically, these projects involve both buildings and the infrastructure that supports them. Construction engineers may collaborate with other engineers, and also manage building crews, to ensure the project is successful.")

    with tab7:
        st.subheader("FACT 7")
        st.write(
            "Materials engineering – the finishing touches: Professionals who specialize in this type of civil engineering in Idaho work with paints, finishes and building materials, such as concrete and metal, to create the best materials solutions for various projects. Materials engineers work with metals, ceramics, and plastics to create new materials. Materials engineers develop, process, and test materials used to create a range of products, from computer chips and aircraft wings to golf clubs and biomedical devices.")
        st.write(
            "Understanding the relationships between properties, structure, processing and performance makes the Materials Engineer the master of the engineering universe. Materials science teaches us what things are made of and why they behave as they do. Materials engineering shows us how to apply knowledge to make better things and to make things better. Materials science and engineering drives innovation in both research and industry in everything from aerospace to medicine.")

    with tab8:
        st.subheader("FACT 8")
        st.write(
            "Earthquake engineering – keeping things stable: Not everyone knows this fun fact. Some civil engineers in Idaho specialize in reducing earthquake risk. Engineers must design in structures that can absorb the energy of the waves throughout the height of the building.")
        st.write(
            "Earthquake engineering is the specialization within the Civil Engineering discipline that deals with the various technological processes, designs, equipment and strategies for making products that can withstand, monitor, predict and analyse earthquakes.")

    with tab9:
        st.subheader("FACT 9")
        st.write(
            "University of Santo Tomas: The first university in the Philippines that offered Civil Engineering program.")
        st.write(
            "The Faculty of Engineering of the University of Santo Tomas (UST) is the oldest engineering school in the Philippines. It was established on May 18, 1907, as School of Civil Engineering with one program offering leading to the degree of Master of Science in Civil Engineering (MSCE)..")

    with tab10:
        st.subheader("FACT 10")
        st.write(
            "Nora Stanton Blatch – first female civil engineer: Cornell University awarded this woman a civil engineering degree in 1905, making her the first female to attain this particular achievement.")
        st.write(
            "She might be the first American female civil engineer, but she was born in England. She showed the world what women empowerment looked like in the era where men were given preference in everything, especially in the engineering field. Nora Stanton Blatch paved the way for women in many areas, not only engineering. What we initially saw as a setback has now become an opportunity to learn and grow. Many other female figures have been inspired by her determination and can-do attitude to follow their dreams.")

    with tab11:
        st.subheader("FACT 11")
        st.write(
            "Institution of Civil Engineers – started in a London coffee shop: The ICE was founded by eight civil engineers. The youngest of these founders was just 19 years old.")
        st.write(
            "In 1818, a small group of young engineers met in a London coffee shop and founded the Institution of Civil Engineers (ICE), the world's first professional engineering body. They had hoped that lots of engineers from different engineering backgrounds would join the institution. Currently, with 95,000 members worldwide, the ICE exists to improve lives by ensuring the world has the engineering capacity and infrastructure systems it needs to enable our planet and our people to thrive.")

    with tab12:
        st.subheader("FACT 12")
        st.write(
            "American Society of Civil Engineers – oldest society of engineers: The ASCE has the longest history of all national engineering societies in the US. Founded in 1852, it is still active today.")
        st.write(
            "Up to date, the American Society of Civil Engineers represents more than 150,000 members of the civil engineering profession in 177 countries. ASCE stands at the forefront of a profession that plans, designs, constructs, and operates society's economic and social engine – the built environment – while protecting and restoring the natural environment.")


    with tab13:
        st.subheader("FACT 13")
        st.write(
            "Creativity is the most important thing for civil engineer. It could be said broadly that the role of Civil Engineers is applying Engineering principles to develop solutions within the built environment. Engineers need to be able to innovate and improve solutions. ")
        st.write(
            "In order to successfully solve problems, engineers must be creative. An inventive mindset is essential for them to design new products and services or improve upon those that have already been created. Engineers need to constantly innovate in order to continue to drive economic and societal successes. Creative engineers are trailblazers who are curious about the possibilities, according to the Knowledge Network for Innovations in Learning and Teaching. Curiousity leads engineers to ask questions, imagine possibilities, conduct experiments and build protypes.")


    with tab14:
        st.subheader("FACT 14")
        st.write(
            "John Smeaton – the first civil engineer: Smeaton constructed the Eddystone Lighthouse and was the first civil engineer who is often referred to as the 'Father of Civil Engineering'.")
        st.write(
            "He worked to create windmills and waterwheels during the Industrial Revolution and published a paper about the correlation between pressure and velocity for objects moving through the air. The term 'civil engineer' was established by John Smeaton in 1750 to contrast engineers working on civil projects with the military engineers, who worked on armaments and defenses.")

    with tab15:
        st.subheader("FACT 15")
        st.write("CODE OF ETHICS: FUNDAMENTAL PRINCIPLES")
        st.write(
            "Civil engineers uphold and advance the integrity, honor and dignity of the civil engineering profession by:")
        st.write("1. using their knowledge and skill for the enhancement of human welfare and the environment;")
        st.write(
            "2. being honest and impartial and serving with fidelity the public, their employers/employees and clients;")
        st.write("3. striving to increase the competence and prestige of the civil engineering profession; and")
        st.write("4. supporting the professional and technical societies of their disciplines.")


if selected== "Infrastructure":
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = ("https://assets3.lottiefiles.com/packages/lf20_ZWN3RI.json")
    lottie_json = load_lottieurl(lottie_hello)
    st_lottie(lottie_json)
    st.write("----------------------------------------")
    st.title('FAMOUS INFRASTRUCTURE IN THE PHILIPPINES')
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20 = st.tabs(
        ["INFRASTRUCTURE 1", "INFRASTRUCTURE 2", "INFRASTRUCTURE 3", "INFRASTRUCTURE 4", "INFRASTRUCTURE 5",
         "INFRASTRUCTURE6", "INFRASTRUCTURE 7", "INFRASTRUCTURE 8", "INFRASTRUCTURE 9", "INFRASTRUCTURE 10",
         "INFRASTRUCTURE 11", "INFRASTRUCTURE 12", "INFRASTRUCTURE 13", "INFRASTRUCTURE 14", "INFRASTRUCTURE 15",
         "INFRASTRUCTURE 16", "INFRASTRUCTURE 17", "INFRASTRUCTURE 18", "INFRASTRUCTURE 19", "INFRASTRUCTURE 20"])

    with tab1:
        st.subheader("Mactan-Cebu International Airport")
        st.write(
            "Mactan–Cebu International Airport (Cebuano: Tugpahanang Pangkalibutanon sa Mactan–Sugbo; Filipino: Paliparang Pandaigdig ng Mactan–Cebu; IATA: CEB, ICAO: RPVM) is an international airport serving Metro Cebu and serves as the main gateway to the Central Visayas region. Located on a 797-hectare (1,970-acre) site in Lapu-Lapu City on Mactan, it is the second busiest airport in the Philippines.[3] The airport serves as a hub for Cebu Pacific, Pan Pacific Airlines, Philippine Airlines and Royal Air Philippines, and as a base for Philippines AirAsia. The airport is managed by the Mactan–Cebu International Airport Authority and operated by the GMR–Megawide Cebu Airport Corporation.")
        with st.expander("Architecture and Design"):
            st.write(
                "The terminal was designed by Hong Kong-based Integrated Design Associates, with local designers Budji Layug, Royal Pinda, and Cebu’s Kenneth Cobonpue. The roof, which is made out of wood, is the most recognisable element. The structure is composed of an array of glulam (glue-laminated) arches, which form the roof curvature and define its geometry and modularity.")
            st.write(
                "The arches span every 30 metres allowing the terminal to be as column-free as possible. The white alpine’s wood has a service life of about 200 years and requires a protective coating every 50 years.")
            st.write(
                "The retail area in the terminal spans approximately 3,000sq m, and features an 895sq m walk-through duty free store operated by Duty Free Philippines which complements the look and feel of the terminal.")
            st.write(
                "The new terminal features prominently in a special eZine dedicated to the fast-changing travel retail market in the Philippines published by The Moodie Davitt Report.")


    with tab2:
        st.subheader('National Arts Center')
        st.write(
            'The National Arts Center is a building complex situated in Mount Makiling, Los Baños, Laguna, the Philippines. The establishment was inaugurated in 1976. Its theater is the Tanghalang Maria Makiling or the NAC Center, which has an audience capacity of 1,000 people.')
        st.write(
            'The complex occupies a total area of 13.5 hectares (33 acres) at the Makiling Forest Reservation. Most of its facilities are operated by the Philippine High School for the Arts except the Pugad Adarna, which is run by the Cultural Center of the Philippines.')
        st.write(
            "Venues aside from the theater include the Pugad Aliguyon or the Marvilla Cottages, the Pugad Adarna or Executive House, a two-story clubhouse called the Bulwagang Sarimanok, and the St. Marc's Chapel. The chapel's cross was designed by Leandro Locsin and features an outline of a crucified Jesus Christ.")
        with st.expander('   Architecture and Design '):
            st.write(
                'Designed by acclaimed Filipino architect Leandro V. Locsin, the National Arts Center in Laguna represents a modern reinterpretation of the indigenous, vernacular architecture of the region. Often crafting bold, monolithic forms with simple geometries, Locsin’s Center deliberately focuses upon the roof form, relating domestic Cordilleran architecture to a much more substantial mass.')

    with tab3:
        st.subheader('National Museum of Fine Arts')
        st.write(
            "The National Museum of Fine Arts (Filipino: Pambansang Museo ng Sining), formerly known as the National Art Gallery, is an art museum in Manila, Philippines. It is located on Padre Burgos Avenue across from the National Museum of Anthropology in the eastern side of Rizal Park. The museum, owned and operated by the National Museum of the Philippines, was founded in 1998 and houses a collection of paintings and sculptures by classical Filipino artists such as Juan Luna, Félix Resurrección Hidalgo and Guillermo Tolentino.")
        st.write(
            "The neoclassical building was built in 1921 and originally served to house the various legislative bodies of the Philippine government. Known as the Old Legislative Building (also the Old Congress Building), it was the home of the bicameral congress from 1926 to 1972, and the Philippine Senate from 1987 to 1997.")
        with st.expander('Architecture and Design'):
            st.write(
                "Along Padre Burgos Street heading southwest, the monumental Old Legislative Building is presently the National Museum of Fine Arts.  The building designed by Ralph Harrington Doane, Antonio Mañalac Toledo and Juan M. Arellano was built between 1918-1926.  Doane with the assistance of Toledo, designed the building originally as the National Library. The building began its construction in 1918, was delayed for lack of funds, and was decided to become the Legislative Building. Arellano revised the plan by adding the fourth floor and the chambers for legislators, changing the central façade and incorporating the ornamentation and sculptural work.")
            st.write(
                "In February 1945 the Japanese forces used the building and its premises as their stronghold and modified it with their defensive installations. Obstacles, roadblocks, trenches, pillboxes and barbed wires surrounded the building. Guns and other heavy machine guns were strategically installed on the building floors. For several days until February 27 the American forces bombarded the building with artillery fire. The building’s north and south wings were heavily damaged.")
            st.write(
                "The building was rebuilt in 1949, maintaining its original building footprint and four-story height, but with less ornate façade articulation. The four-story building has a rectangular plan and layout oriented with its line of symmetry in an east-west axis, longitude in a north-south axis, and its main entrances on the east and the west. The building’s central core spaces are flanked by courtyards north and south. The associated rooms are organized around these courtyards with single volume hallways east and west, and double volume hallways north and south. Staircases are at both ends of the entrance halls, and the four corners of the building.")
            st.write(
                "The columned portico at the second floor signals the west entrance accessed through the flights of stairs and the carriageway ramp coming from the ground level along Padre Burgos Street. The west portico has four Corinthian columns rising the full height of the building.")
            st.write(
                "The façades are articulated with giant Corinthian columns and pilasters rising from the second floor level to the height of the two stories of the building, with the first story resembling the one-story high plinth where these columns and pilasters rest.")
            st.write(
                "Decorative entablatures lie above the columns and pilasters surrounding the entire wall.  The projecting central bay features a group of four columns, with corbeled balconies on the third level. The corner bays feature another group of four columns with similar Corinthian capitals. Fenestrations feature rectangular windows decorated with grillework. Both east and west façades are identical except for the west central bay with the columned portico. Surmounting the central part of the building are identical east and west pediments with relief sculptures. The temple pediment with relief sculptures depicting “Inang Bayan” surrounded by Greek deities on its tympanum emphasizes grandeur and nationalism, and ennobles the edifice. A splendid view of Intramuros and Luneta can be enjoyed from the west and south of the building respectively.")
            st.write(
                "The building’s east façade is identical with the west façade except for the central bay. An arched porte-cochere protects the east entrance at the ground level approached by way of the east driveway from the present east open space (formerly a southward radial road with Agrifina Circle as its terminus).")
            st.write(
                "As the present National Museum of Fine Arts, new additions north and south of the building footprint serve as the museum building’s administrative offices, and public spaces. Sculptures accentuates the building’s grounds and open spaces.  The open spaces east of the building serve as a visual corridor where one can enjoy the perspectives of the surrounding urban spaces and the other neo-classical building across the road, the present National Museum of Anthropology (former Department of Finance Building).")
            st.write(
                "Today, the building as the National Museum of Fine Arts, is a home to 29 galleries and hallway exhibitions comprising of 19th century Filipino masters, National Artists, leading modern painters, sculptors, and printmakers. Also on view are art loans from other government institutions, organizations, and individuals.")

    with tab4:
        st.subheader('Parish of the Holy Sacrifice')
        st.write(
            'The Parish of the Holy Sacrifice, also known as the Church of the Holy Sacrifice, is a landmark Catholic chapel on the University of the Philippines Diliman campus. It belongs to the Roman Catholic Diocese of Cubao and its present parish priest is Rev. Fr. Jose S. Tupino III. More popularly known as the UP Chapel, the church was constructed under the supervision of Fr. John P. Delaney, who began ministering to the spiritual needs of the campus in 1947.')
        st.write(
            'Known for its architectural design, the church is recognized as a National Historical Landmark and a Cultural Treasure by the National Historical Commission of the Philippines, and the National Museum of the Philippines respectively. It was designed by the late National Artist of the Philippines for Architecture, Leandro Locsin, one of four National Artists who collaborated on the project. According to a post from the UP Diliman website, it is the only structure in the country where the works of five national artists can be found. Alfredo Juinio served as the structural engineer for the project.')
        st.write(
            "The church is adjacent to the U.P. Health Service Building and the U.P. Shopping Center, and is serviced by all of the university's jeepney routes.")
        with st.expander("Architecture and Design"):
            st.write(
                'Initially, Leandro Locsin designed the church for the Ossorio family, who were planning to build a chapel in Negros. Unfortunately, the plans for the chapel were scrapped when Frederic Ossorio, the head of the family, left for the United States. However, in 1955, Father Delaney commissioned Locsin to design a chapel that was open and could easily accommodate 1,000 people. The Church of Holy Sacrifice became the first circular chapel with the altar in its center in the country, and the first to have a thin shell concrete dome. This was his first major architectural commission.')
            st.write(
                'Locsin chose the round plan as the most suited for giving the congregation a sense of participation in the mass. The center of the plan is the altar, which is elevated from the floor by three steps. The separation of the choir and congregation was dissolved through this design. The ceiling of the concrete dome church was left bare and a dramatic use of colored lights mark the changing seasons of worship.')
            st.write(
                'The dome of the church is supported by thirty two columns located along its rim. These columns terminate a third of the way up where they support the ledge-like ring beam. This ring beam, in turn, supports the 3-inch thick concrete shell of the dome that spans 29.26 metres (96.0 ft). The unique design of the dome allows in natural lighting and ventilation. In the middle of the dome is a circular skylight, which supports the triangular bell tower. The bell tower, then extends to the interior, supporting the crucifix. The arrangement of the interior of the church is concentric, with the altar in the middle.')
            st.write(
                'The fifteen murals depicting the Stations of the Cross that adorn the circular walls are by Vicente Manansala assisted by Ang Kiukok. The fifteenth mural of the "Resurrection of Christ" is on the wall of the sacristy. The cross depicting both a suffering and a risen Christ and the marble altar are the handiwork of Napoleon Abueva. The floor mural, executed in terazzo and radiating from the altar, is by Arturo Luz. This floor mural is also called the "River of Life". Fernando Zobel de Ayala had studies to fill the outer wall with calligraphic interpretations. However, the project was not executed. In 1968, Jose Maceda, another national artist, premiered his concert, Pagsamba at the PHS, and repeated it in 1978 and 1998 at the same venue.')
            st.write(
                'On January 12, 2005, the church was recognized as a National Historical Landmark and a Cultural Treasure by the National Historical Institute and the National Museum, respectively. During the recognition ceremony, National Historical Institute Chairman Ambeth R. Ocampo lauded the church as a "masterpiece of Filipino artistry and ingenuity".Currently, a project aims to restore the dome of the historic church.')
            st.write(
                'On March 26, 2021, the church was repaired and repainted. The rehabilitation project started in 2020 through a series of consultations with UP officials in an effort to bring back the 65-year-old cultural treasure’s original state of beauty. Developer DMCI Homes facilitated the following repairs in the chapel: repair of masonry cracks; de-clogging of downspouts and drains; installation of new electrical fixtures; and, exterior repainting on the chapel’s iconic dome and roof, as well as of its walls, columns, eaves, under slabs, ceilings, and railings.')
            st.write(
                "The murals depicting the Stations of the Cross, the marble altar, the floor mural, and the cross at the center of the chapel—all handiworks of national artists—were left untouched during the rehabilitation")


    with tab5:
        st.subheader('Philippine International Convention Center')
        st.write(
            'The Philippine International Convention Center (Filipino: Sentrong Pangkumbensyong Pandaigdig ng Pilipinas, or PICC) is a convention center located in the Cultural Center of the Philippines Complex in Pasay, Metro Manila, Philippines. The facility has been the host of numerous local and foreign conventions, meetings, fairs, and social events. The PICC served as the office of the Vice President of the Philippines until 2005. It also previously housed the Philippine Charity Sweepstakes Office.')
        with st.expander('Architecture and Design'):
            st.write(
                'The Philippine International Convention Center is composed of five building modules: the Delegation Building, Secretariat Building, Plenary Hall, Reception Hall and The Forum. The facility, which was designed by Leandro Locsin, who would be later named National Artist was built in reclaimed land and has a floor area of more than 65,000 sq ft (6,000 m2).')


    with tab6:
        st.subheader('San Miguel Corporation Building')
        st.write(
            "San Miguel Corporation, abbreviated as SMC, is a Philippine multinational conglomerate headquartered in Mandaluyong, Metro Manila. The company is one of the largest and most diversified conglomerates in the Philippines. Originally founded in 1890 as brewery in the Philippines, San Miguel has ventured beyond its core business, with investments in various sectors such as food and drink, finance, infrastructure, oil and energy, transportation, and real estate.")
        st.write(
            "Its flagship product, San Miguel Beer, is one of the largest selling beers in the world. San Miguel's manufacturing operations have extended beyond its home market to Hong Kong, China, Indonesia, Vietnam, Thailand, Malaysia, and Australia, and its products are exported to 60 markets around the world.")
        with st.expander("Architecture and Design"):
            st.write(
                "Designed by the Mañosa brothers (Manuel, Francisco, and Jose), the San Miguel Corporation Building in Ortigas serves as the head office of one of the largest corporations in the Philippines. The building’s unique design is inspired by the Banaue rice terraces. Landscaping is done by the National Artist for Architecture in 2006, Ildefonso Santos, who is considered the father of Philippine landscape architecture.")

    with tab7:
        st.subheader('SM Mall of Asia Arena')
        st.write(
            "The SM Mall of Asia Arena, also known as the Mall of Asia Arena or the MoA Arena, is an indoor arena within the SM Mall of Asia complex, in Bay City, Pasay, Metro Manila, Philippines. It has a seating capacity of 15,000 for sporting events, and a full house capacity of 20,000. The Arena officially opened on May 21, 2012. It has retractable seats and a 2,000-capacity car park building.")
        st.write(
            "The SM Mall of Asia Arena is the alternate venue of the Philippine Basketball Association when the Smart Araneta Coliseum in Quezon City is unavailable. The arena is also one of the main venues for the University Athletic Association of the Philippines and the National Collegiate Athletic Association.")
        with st.expander('Architecture and Design'):
            st.write(
                "The SM Mall of Asia Arena was designed by architecture firm Arquitectonica. The facility was intended primarily as a venue for concerts and basketball games but can be reconfigured to accommodate other sporting and entertainment events as well. It has a seating capacity of 15,000 but can host as much as 20,000 people in a full-house capacity.")
            st.write(
                "The indoor arena stands on a 16,000 sq m (170,000 sq ft) had a floor area of 52,000 sq m (560,000 sq ft). The limited area of the site meant that part of the building to span over the adjacent Pacific Drive. Due to a high water table, the construction of basement parking levels was limited and a separate eight-storey parking building called Mall of Asia Arena Annex (MAAX) which can accommodate 1,400 vehicles had to be built. The façade of the building are covered with low-e coated and fritted insulated glass units.")
            st.write(
                "The structure hosting the events space was designed in a form of an eye which was supported by a slanted podium plinth.")
            st.write(
                "The venue uses NBA-specification shot clocks, with Daktronics BB-2140 and BB-2141 shot clocks (used by the NBA along with models from OES until the 2016–17 NBA season due to the NBA using Tissot ones) that count tenths in the final five seconds, though recently it has been stretched to the final nine seconds.")


    with tab8:
        st.subheader("St. Augustine Church")
        st.write(
            "The Church of Saint Augustine (Filipino: Simbahan ng San Agustin, Spanish: Iglesia de San Agustín), also known as the Archdiocesan Pontifical Shrine of Our Lady of Consolation and Cincture (Spanish: Santuario Pontificale Arquidiocesano de Nuestra Señora de la Consolación y Correa) or the Immaculate Conception Parish (Filipino: Parokya ng Imakulada Conception, Spanish: Parroquia de la Inmaculada Concepción), is a Roman Catholic church under the auspices of the Order of Saint Augustine located inside the historic walled city of Intramuros in Manila, Philippines. Completed in 1607, it is the oldest stone church in the country.")
        st.write(
            "In 1993, San Agustin Church was one of four Philippine churches constructed during the Spanish colonial period to be designated as a World Heritage Site by UNESCO, under the collective title Baroque Churches of the Philippines. It was named a National Historical Landmark by the Philippine government in 1976.")
        with st.expander("Architecture and Design"):
            st.write(
                "The San Agustin Church is patterned after some of the magnificent temples built by the Augustinians in Mexico. The present edifice was built in 1587, and completed, together with the monastery, in 1604. The atmosphere is medieval since 'both church and monastery symbolize the majesty and equilibrium of a Spanish golden era.'")
            st.write(
                "The massive structure of the church is highlighted by the symmetry and splendor of the interiors (painted by two Italians who succeeded in producing trompe l'oeil) – the profile of the mouldings, rosettes and sunken panels which appear as three-dimensional carvings, a baroque pulpit with the native pineapple as a motif, the grand pipe organ, the antechoir with a 16th-century crucifix, the choir seats carved in molave with ivory inlays of the 17th century and the set of 16 huge and beautiful chandeliers from Paris.")


    with tab9:
        st.subheader('The Mind Museum')
        st.write(
            'It is a 5,000 square meter exhibit area located in a12,500 square meter JY Campos Park in Bonifacio Global City. It is the first world-class science museum in the Philippines. The museum opened on March 16, 2012,[2] although a pre-launch reception was held a year earlier on December 15 where Vice President Jejomar Binay delivered a speech on behalf of President Benigno Aquino III.[3] The facility was developed by the Bonifacio Art Foundation Inc (BAFI).')
        with st.expander('Architecture and Design'):
            st.write(
                'The museum was designed by architect Ed Calma, from Lor Calma & Partners. Th design of the structure was inspired from cellular structure and growth and had a solar reflective exterior, natural wind ventilation and rainwater flow drainage. With assistance from a firm based in the United States, which did the master plan of the museum, Filipino designers, scientists and fabricators did 90 percent of the museums exhibits. The designers included designers and faculty from the College of Fine Arts of the University of the Philippines and the University of Sto. Tomas. ')
            st.write(
                'The goal of the Science Museum is to convey important and accurate science principles through the use of interactive, multi-media and multi-sensory exhibits firmly based in a story context. Current story topics include The Universe, Life, Nature, The Atom and Technology Each of the major exhibit galleries, or “spheres,” includes an iconic “centerpiece” surrounded by 25 to 30 exhibits embedded within the overall gallery aesthetic and/or architecture. Corridors connecting the five spheres provide further opportunities for interpretation and immersion within the various story themes.')


    with tab10:
        st.subheader('Zuellig Building')
        st.write(
            'The Zuellig Building is an office skyscraper located in the Makati Central Business District in Metro Manila, Philippines, and is one of buildings taller than 150 m in the area. It is owned by the Zuellig Group and developed by its real estate arm, Bridgebury Realty Corp. It rises to 160 meters (520 ft),and was the first Platinum level LEED Core and Shell building in the Philippines upon its completion in 2013.')
        with st.expander('Architecture and Design'):
            st.write(
                'The Zuellig Building was designed by international architectural firm Skidmore, Owings and Merrill, in cooperation with local architectural firm W.V. Coscolluela & Associates. Facade design was done by Meinhardt Hong Kong Pte. Ltd., while Structural, Mechanical & Electrical, and Fire Protection engineering & design was provided by Meinhardt Philippines.')
            st.write(
                'Other consultants of the project team are Davis Langdon & Seah Philippines Inc. (LEED Sustainability Consultant); E.A Aurelio Landscape Architects (Landscape Consultant); SBLD Studio (Lighting Consultant); Hill & Associates Risk Consulting (Philippines) Inc. (Security Consultant); and Sun Asia Industries (Traffic Consultant).')
            st.write(
                'The general contractor is Leighton Contractors (Philippines). The project construction team also includes Permasteelisa (Curtain Wall Installation); Design Coordinates, Inc.(Construction Project Management); and Davis Langdon & Seah Philippines, Inc. (Quantity Surveying).[1]')


    with tab11:
        st.subheader(" CULTURAL CENTER OF THE PHILIPPINES ")
        st.write(' The Cultural Center of the Philippines (Filipino: Sentrong Pangkultura ng Pilipinas, or CCP) is a '
                 'government-owned and controlled corporation established to preserve, develop and promote arts and culture '
                 'in the Philippines. The CCP was established through Executive Order No. 30 s. 1966 by President Ferdinand'
                 ' Marcos. Although an independent institution of the Philippine government, it receives an annual subsidy and'
                 ' is placed under the National Commission for Culture and the Arts for purposes of policy coordination. The'
                 ' CCP is headed by Chairperson Margarita Moran-Floirendo. Its current president is Arsenio Lizaso.')

        st.write(
            ' The CCP provides performance and exhibition venues for various local and international productions at the'
            ' 62-hectare (150-acre) Cultural Center of the Philippines Complex located in the cities of Pasay and '
            'Manila. Its artistic programs include the production of performances, festivals, exhibitions, cultural '
            'research, outreach, preservation, and publication of materials on Philippine art and culture. It holds its'
            ' headquarters at the Tanghalang Pambansa (English: National Theater), a structure designed by National '
            'Artist for Architecture, Leandro V. Locsin. Locsin would later design many of the other '
            'buildings in the CCP Complex.')
        with st.expander(' Architecture and Design '):
            st.write('  Designed by Leandro Locsin, the CCP massive, rough concrete edifice, in the style of Brutalist'
                     ' architecture, took four years to build on 21 hectares of reclaimed land along Manila Bay. Envisioned'
                     ' by then First Lady Imelda Marcos as a showcase of Filipino artistic expression and an architectural'
                     ' landmark. ')

            st.write(
                ' The facade of the National Theater is dominated by a two-storey travertine block and deep concave'
                ' cantilevers on three sides. It is clad by concrete textured by crushed seashells.')


    with tab12:
        st.subheader(" CALLE CRISOLOGO ")
        st.write(
            ' Calle Crisologo owes its name to the illustrious Ilocano poet, writer, and playwright Governor Marcelino'
            ' “Mena” Crisologo. Previously, the street was called Calle de Escolta de Vigan, whose residents were mostly'
            ' families who profited from the galleon trade that included Ilocos as a key port. When Governor Crisologo'
            ' died in 1927, the street was renamed Calle Crisologo in his honor. The street is part of Vigan’s'
            ' picturesque Heritage Village, a UNESCO World Heritage Site. This consists of about 200 beautifully restored'
            ' houses dating back to the 16th century. The buildings on Crisologo particularly display a blend of '
            'indigenous Filipino and colonial European construction.')

        st.write(
            ' It took 10 years for Vigan to be named a World Heritage Site since it was submitted for consideration'
            ' in 1989. The town was initially rejected for inclusion reportedly because it could not compare with '
            'Spanish-Colonial cities such as Cartagena in Colombia and Trinidad in Cuba. Local advocates campaigned '
            'that Vigan’s architectures more similarly reflect those of old Asian trading cities like Hoi An, '
            'Malacca, or Macau. In fact, many houses in Calle Crisologo were owned not only by scions of Spanish'
            ' settlers but also by wealthy Chinese who migrated to Ilocos Sur to set up businesses. ')

        with st.expander(' Architecture and Design '):
            st.write(
                ' Architectural Style: Spanish Colonial with Chinese embellishments and intricate architectural details. '
                'The whole stretch of the street is paved with cobblestones. This world famous historic street located in'
                'the Mestizo district of Vigan City is a stretch of mixed-use residential buildings. The ground floor is'
                ' used for family-owned shops and/or restaurants while the upper floor is the family’s residence. The '
                'daylight sun from morning to the afternoon reveals the rich beauty of the street with the structures’'
                ' details shadowing the whole stretch, while intricate ornamental antique lightings accentuate the '
                'window,doors, walls and the pavements at night. ')
            st.write(
                '  It boasts centuries-old stone houses, lovely tungsten lamps, and antique cobblestone, where horse-drawn'
                ' carriages or kalesas are still used for transport. In fact, the street is a pedestrian-only zone, save '
                'for kalesas favored for touring the historical sites around town. ')



    with tab13:
        st.subheader(" THE RUINS MANSION ")
        st.write(
            ' The Ruins was the ancestral mansion of the family of wealthy sugar businessman Don Mariano Ledesma Lacson'
            ' built on a 440 hectare sugar plantation in Talisay City, Negros Occidental, in the early 1900s in memory '
            'of his Portuguese wife Maria Braga Lacson, who died during the birth of their 8th child. During the Second '
            'World War, Filipino guerillas burned it down as a countermeasure to prevent the invading Japanese forces '
            'from using it as a military headquarters. It burned for three days. The intention was to burn it to the'
            ' ground. ')

        st.write(' This is known variously as the "Taj Mahal of Talisay", "Taj Mahal of Negros" and "Taj Mahal of the '
                 'Philippines", it is in the private ownership of the great-grandchildren of Don Mariano Ledesma Lacson and '
                 'Cora Maria Osorio Rosa-Braga. They have preserved it in its ruined state, among operational farmland, as a'
                 ' tourist attraction that can be visited for a fee or hired for events. It is open to daily visitors from'
                 ' 8am to 8pm for am entrance fee of PHP100 for adults, PHP 50 for students and PHP20 for children.')

        with st.expander(" Architecture and Design "):
            st.write(
                ' The structure of what’s left of the mansion is that we now call The Ruins, withstood the test of time'
                ' mainly due to the oversized steel bars and the A-grade mixture of concrete used in its construction.'
                '  The wall finishing which were made of egg whites mixed with cement gave it its marble-like '
                'appearance.')
            st.write(
                ' The structure of The Ruins is of Italianate architecture with neo-Romanesque columns, having a very '
                'close semblance to the facade of Carnegie Hall in New York City. The intricate designs of the columns'
                ' are still very intact and quite impressive. Whoever made those designs is truly a master in the art.')



    with tab14:
        st.subheader(" INTRAMUROS ")
        st.write(
            ' Intramuros (Latin for "inside the walls") is the 0.67-square-kilometer (0.26 sq mi) historic walled area'
            ' within the city of Manila, the capital of the Philippines. It is administered by the Intramuros '
            'Administration with the help of the city government of Manila.')

        st.write(
            ' Present-day Intramuros comprises a centuries-old historic district, entirely surrounded by fortifications,'
            ' that was considered at the time of the Spanish Empire to be the entire City of Manila. Other towns and '
            'arrabales (suburbs) located beyond the walls that are now districts of Manila were referred to as '
            'extramuros, Latin for "outside the walls", and were independent towns that were only incorporated'
            ' into the city of Manila during the early 20th century. Intramuros served as the seat of government of '
            'the Captaincy General of the Philippines, a component realm of the Spanish Empire, housing the colonys'
            ' governor-general from its founding in 1571 until 1865, and the Real Audiencia of Manila until the end '
            'of Spanish rule during the Philippine Revolution of 1898.')

        st.write(' The walled city was also considered the religious and educational center of the Spanish East Indies.'
                 ' The original campuses of the University of Santo Tomas, the oldest university in Asia, and the Ateneo'
                 ' de Manila, were in Intramuros before transferring in 1927 and 1932 respectively; today the area still '
                 'contains the main campuses of the University of the City of Manila, the Colegio de San Juan de Letran, '
                 'Mapúa University, Philippine Nautical Training Colleges, the Colegio de Santa Rosa, and the Manila High'
                 ' School. Intramuros was also an economic center; its port in what is now Plaza Mexico was the Asian '
                 'hub of the Manila galleon trade, carrying goods to and from Acapulco in what is now Mexico.')

        with st.expander(" Architecture and Design "):
            st.write(
                ' Intramuros, or the ‘Walled City’, is one of the oldest districts of Manila, built on the south bank'
                ' of the Pasig River around 1571. It was built by the Spaniards – more specifically by Miguel Lopez de'
                ' Legaspi – and is bound on all sides by moats and thick, high walls, with some over 6 metres high.')

            st.write(
                ' Intramuros fortification was designed as a trapezoidal layout, located on a wedge formed by the sea'
                ' and the Pasig River (now the land reclamation difficults that reading). Inside the walls there is a'
                ' rectangular gridiron, which included the main square, surrounded by the major powers of the time: '
                'the cathedral, the prison the house of the governor. In that sense, Intramuros is similar to other'
                ' fortified cities in Latin America, such as Lima , for example.')



    with tab15:
        st.subheader(" MANILA HOTEL")
        st.write(
            ' Manila Hotel is a beautiful 5-star hotel located in Manila just 701 m from iconic Intramuros and 901 m '
            'from Manila Cathedral. The hotel provides free Wi-Fi access and facilities like in-house dining options, a'
            ' business center and an outdoor swimming pool.')

        st.write(
            ' Rooms are elegantly decorated and provide guests with a flat-screen TV, air conditioning and a seating area.'
            ' Featuring a shower, the private bathrooms also come with a bath and a hairdryer. The suites have an ipod '
            'docking station, bathrooms fitted with Italian marble and a senso-memory foam mattress. Some rooms offer '
            'views of Manila Bay, while other offer views of the city.')

        with st.expander(" Architecture and Design "):
            st.write(
                ' The Manila Hotel is situated in the heart of the City of Manila. William Howard Taft created an urban'
                ' plan for the city of Manila. He hired Architect Daniel Hudson Burnham who drafted a wide and long '
                'tree-lined boulevard that would begin at the park where the end of the bay would be dominated by a '
                'magnificent hotel. To execute Burnham’s plans, Taft hired William E. Parsons, a New York city architect,'
                ' who envisioned an impressive, comfortable hotel which he patterned along the lines of Californian '
                'mission style architecture. ')

            st.write(
                ' Measuring 125 feet (38 m) long by 25 feet (7.6 m) wide, the lobby is lined with white Doric columns.'
                ' The floor is Philippine marble; the chandeliers are made of brass, crystal, and seashells; the furniture'
                ' is carved out of Philippine mahogany, which is used throughout the hotel.')


    with tab16:
        st.subheader(" SAN JUANICO BRIDGE ")
        st.write(
            ' The San Juanico Bridge (Filipino: Tulay ng San Juanico; Waray: Tulay han San Juanico) is part of the '
            'Pan-Philippine Highway and stretches from Samar to Leyte across the San Juanico Strait in the Philippines. '
            'Constructed during the administration of President Ferdinand Marcos through Japanese Official Development'
            ' Assistance loans, it has a total length of 2.16 kilometers (1.34 mi)—the second longest bridge spanning a '
            'body of seawater in the Philippines after Cebu-Cordova Bridge.')

        st.write(
            ' Marcos built the bridge as a personal gift to his wife Imelda using public funds siphoned through the'
            ' controversial Marcos Japanese ODA scandal. It was one of the high-visibility foreign-loan projects'
            ' initiated by Marcos during the run-up to the 1969 presidential election. Completed four years later, it'
            ' was inaugurated on 2 July 1973 on the birthday of Imelda Marcos. Upon its completion, economists and'
            ' public works engineers quickly tagged it as a white elephant which was "a possession that is useless '
            'and expensive to maintain or difficult to dispose of", because its average daily traffic was too low to'
            ' justify the cost of its construction.')

        with st.expander(' Architecture and Design '):
            st.write(
                ' San Juanico Bridge’s is made of a steel girder viaduct built on reinforced concrete piers, and its '
                'main span is of an arch-shaped truss design. It has 43 spans and its large main arch rises 41 meters '
                'above the sea level. It is considered one of the most beautifully designed bridges in Philippines.')



    with tab17:
        st.subheader(" PHILIPPINE HEART CENTER ")
        st.write(
            ' The Philippine Heart Center is a hospital specializing in the treatment of heart ailments. It has rooms for'
            ' paying patients and charity patients and admits more than 14,000 patients every year, including 3,300 that'
            ' undergo heart surgery. It holds regular training programs for medical professionals.')

        st.write(' The Philippine Heart Center was established through Presidential Decree No. 673 issued by president '
                 'Ferdinand E. Marcos in 1975. The building is identified with what is referred to as the Marcoses' "edifice"
                 " complex,defined by architect Gerard Lico as an obsession and compulsion to build edifices as a hallmark"
                 " of greatness. The hospital was built using 50% of the national health budget, according to Senator Jose W."
                 " Diokno, while around the country, Filipinos were dying of curable illnesses like TB [tuberculosis],"
                 " whooping cough, and dysentery. ")

        with st.expander(' Architecture and Design '):
            st.write(
                ' The Philippine Heart Center is seated on a 2.7 hectare lot at the corner of East Avenue and Matalino'
                ' Street in the Diliman District of Quezon City. It is bounded by the East Avenue Medical Center on its'
                ' side. Other landmarks within the vicinity are: Bangko Sentral ng Pilipinas (Printing and Mint Plant),'
                ' National Kidney and Transplant Institute, Social Security System, Quezon City Hall, Sulo Hotel, among'
                ' others. It has four (4) buildings composed of a five-storey Hospital building, a nine-storey Medical'
                ' Arts building with a two-storey Annex, and the two-storey Nuclear Medicine building. Also, government'
                ' offices like the Development Bank of the Philippines (1st floor) and Tariff Commission (5th floor)'
                ' have their offices here.')

            st.write(' The PHC hospital proper is a 354-bed tertiary care center. There are twenty-one nursing units,'
                     ' including 53 Intensive Care Unit (ICU) beds, 24 suites, 56 private rooms, a presidential suite, 74'
                     ' semi-private rooms, 3 adult service wards, and a pediatric service ward. Its design of having 4 petals'
                     ' in each floor represents the 4 chambers of the human heart.')


    with tab18:
        st.subheader(" CEBU CORDOVA LINK EXPRESSWAY ")
        st.write(
            ' The Cebu–Cordova Link Expressway (CCLEX), also known as the Cebu–Cordova Bridge and the Third Cebu–Mactan'
            ' Bridge (or simply, the Third Bridge), is an 8.9-kilometer (5.5 mi) toll bridge expressway in Metro Cebu,'
            ' Philippines. The bridge connects the South Road Properties in Cebu City in mainland Cebu, and Cordova, on'
            ' Mactan island. Crossing the Mactan Channel, it is the third road link between Cebu and Mactan islands, and'
            ' the first between Cebu City and Cordova. It is the longest sea-crossing bridge in the Philippines,'
            ' surpassing the 2-kilometer (1.2 mi) San Juanico Bridge between Samar and Leyte, as well as Marcelo Fernan'
            ' Bridge (which also crosses the Mactan Channel) as the longest cable-stayed bridge in the Philippines.')

        with st.expander(' Architecture and Design '):
            st.write(
                ' The bridge spans 8.9 kilometers (5.5 mi) and is the longest and tallest bridge in the Philippines,'
                ' surpassing the San Juanico Bridge, which crosses Leyte and Samar, and the Candaba Viaduct along the'
                ' North Luzon Expressway. It was designed by the Spanish firms Carlos Fernandez Casado (CFC) and SENER'
                ' Ingeniería y Sistemas, while the local firm DCCD Engineering Corporation and the Danish firm COWI are'
                ' the owners engineers. The bridge is being built by a joint venture between Spanish firm Acciona, and'
                ' Philippine firms First Balfour and DMCI. Connecting Cebu City and Cordova, the 27-meter-wide (89 ft) '
                'bridge is meant to serve an alternate route serving Mactan–Cebu International Airport, capable of '
                'serving at least 40,000 vehicles daily.')

            st.write(
                ' The 390-meter-long (1,280 ft) main span of the CCLEX is cable-stayed and are supported by 145-meter-'
                'high (476 ft) twin tower pylons. The design of the pylons were inspired from the historic Magellans '
                'Cross Pavilion. The main span will have a 51-meter (167 ft)[2] navigation clearance, which allow ships'
                ' to traverse the bridge. Viaduct approach bridges and a causeway will also form part of the CCLEX, as'
                ' well as toll road facilities on an artificial island. The toll facilities design are inspired from the'
                ' eight-rayed sun of the Philippine flag.')



    with tab19:
        st.subheader(" NATIONAL KIDNEY AND TRANSPLANT INSTITUTE ")
        st.write(' The National Kidney and Transplant Institute (NKTI) is a government-owned and controlled corporate '
                 'tertiary specialty center attached to the Department of Health. Its mandate is to specialize in the '
                 'prevention, diagnosis, rehabilitation and treatment of kidney and allied diseases through dialysis and '
                 'transplantation. It focuses on service, training and research in the field of renal diseases and organ '
                 'transplantation.')

        st.write(
            ' The National Kidney and Transplant Institute is a tertiary referral hospital located in Central, Quezon'
            ' City, Philippines. The hospital opened on January 16, 1981. The National Kidney and Transplant Institute,'
            ' or NKTI, is a tertiary medical specialty center for renal health. The hospital also offers voluntary blood'
            ' services.The hospital was formerly known as the National Kidney Foundation of the Philippines (NKFP), and'
            ' the National Kidney Institute.')

        with st.expander(' Architecture and Design '):
            st.write(
                ' The National Kidney and Transplant Institute sits in the center of a 58,899-square-meter (633,980 sq ft)'
                ' lot, along East Avenue in Quezon City.The Institute itself is 3-storey structure with three buildings '
                '(Main, Annex and Dialysis Center) connected to each other. The Main Building houses most of the Cost '
                'Centers and where the Administrative offices can be found. The Annex Building encloses the recently '
                'opened Marcos Wing and the Radiology Dept (MRI and CT Scan centers), Center for Special Services and '
                'also the ER Dept.')

    with tab20:
        st.subheader(" METRO MANILA SKYWAY ")
        st.write(
            ' The Metro Manila Skyway, officially the Metro Manila Skyway System (MMSS) or simply the Skyway, is an'
            ' elevated highway which is the main expressway in Metro Manila, Philippines. It connects the North and '
            'South Luzon Expressways (NLEX and SLEX) with access to Ninoy Aquino International Airport via the NAIA'
            ' Expressway (NAIAX). It is the first fully grade-separated highway in the Philippines and one of the '
            'longest elevated highways in the world, with a total length of approximately 39.2 kilometers (24.4 mi).')

        st.write(' The expressway runs above major existing highways in Metro Manila and the San Juan River. It passes'
                 ' through the highly urbanized areas of Caloocan, Quezon City, Manila, Makati, Pasay, Taguig, Parañaque,'
                 ' and Muntinlupa, easing congestion on other major thoroughfares. The Skyway is accessible to Class 1 '
                 'vehicles, such as cars, vans, motorcycles above 400 cc (24 cu in), pick-up trucks, and SUVs, and Class 2'
                 ' vehicles and public utility vehicles (PUVs). Previously, Class 2 vehicles and PUVs were banned due to'
                 ' the construction of the extension project.')

        with st.expander(' Architecture and Design '):
            st.write(
                ' The Skyway connects the North and South Luzon Expressways. It runs above several major roads in Metro'
                ' Manila, with strategically located entry and exit ramps. The expressway is divided into stages. Stage'
                ' 3 runs from the North Luzon Expressway, near its Balintawak toll plaza in Caloocan, to Buendia exit'
                ' in Makati; Stage 1 runs from Buendia to Bicutan in Parañaque, and Stage 2 runs from Bicutan to '
                ' Station (Alabang-Zapote) Exit in Alabang, Muntinlupa, and the South Luzon Expressway (SLEX) Elevated'
                ' Extension, formerly known as the Skyway Extension and also known Alabang South Skyway Extension,from'
                ' the Skyway Main Line toll plaza to the South Luzon Expressway near Soldiers Hills in Muntinlupa. '
                'Stages 1 and 2 are collectively known as the South Metro Manila Skyway Project. ')

            st.write(
                ' From 1998 to 2020, the Skyway was a dual elevated carriageway with shoulders on both sides for most of'
                ' its length with six lanes (three in each direction) separated by a median barrier. After the '
                'completion of the Skyway Stage 3 and the SLEX Elevated Extension, the segment from Quirino to Sucat was'
                ' expanded to seven lanes (three lanes northbound and four lanes southbound).[11] In addition, Stage 3'
                ' 2.70-kilometer (1.68 mi) segment from the future San Juan Interchange near the San Juan River to'
                ' Plaza Dilao exit in Manila will be utilized by the future Pasig River Expressway (PAREX). From the '
                'North Luzon Expressway, the SThe Skyway connects the North and South Luzon Expressways. It runs above '
                'several major roads in Metro Manila, with strategically located entry and exit ramps. The expressway'
                ' is divided into stages. Stage 3 runs from the North Luzon Expressway, near its Balintawak toll plaza'
                ' in Caloocan, to Buendia exit in Makati; Stage 1 runs from Buendia to Bicutan in Parañaque, and Stage '
                '2 runs from Bicutan to South Station (Alabang-Zapote) Exit in Alabang, Muntinlupa, and the South'
                ' Luzon Expressway (SLEX) Elevated Extension,[4][9] formerly known as the Skyway Extension and also'
                ' known Alabang South Skyway Extension, from the Skyway Main Line toll plaza to the South Luzon '
                'Expressway near Soldiers Hills in Muntinlupa. Stages 1 and 2 are collectively known as the South '
                'Metro Manila Skyway Project. From 1998 to 2020, the Skyway was a dual elevated carriageway with '
                'shoulders on both sides for most of its length with six lanes (three in each direction) separated by '
                'a median barrier. After the completion of the Skyway Stage 3 and the SLEX Elevated Extension, the '
                'segment from Quirino to Sucat was expanded to seven lanes (three lanes northbound and four lanes s'
                'outhbound). In addition, Stage 3 2.70-kilometer (1.68 mi) segment from the future San Juan Interchange'
                ' near the San Juan River to Plaza Dilao exit in Manila will be utilized by the future Pasig River'
                ' Expressway (PAREX). ')


if selected== "News and Entertainment":
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = ("https://assets1.lottiefiles.com/packages/lf20_yetxuujw.json")
    lottie_json = load_lottieurl(lottie_hello)
    st_lottie(lottie_json)
    st.write("-------------------------------------------")
    st.title('NEWS AND ENTERTAINMENT')
    with st.container():
        image_column, text_column = st.columns((1, 2))

    with text_column:
        st.subheader("Mornings with GMA Regional TV: Top 1 sa Civil Engineer Licensure Exam")
        st.write('Isang Pangasinense, kabilang sa mga nanguna sa katatapos na Civil Engineer Licensure Exam')
        st.markdown("[Watch the Video >](https://youtu.be/Rm6tx_ZrHsc)")

    with st.container():
        image_column, text_column = st.columns((1, 2))


    with text_column:
        st.subheader("Tanod sa Cebu, cum laude sa kursong civil engineering")
        st.write(
            '"Lodi" kung ituring ng kaniyang mga kaklase at guro ang tanod ng Barangay Kalubihan na si Janryll Tan na nagtapos na cum laude sa kursong civil engineering sa isang kolehiyo sa Cebu.')
        st.markdown("[Watch the Video >](https://youtu.be/Jeda0NqVdPM)")

    with st.container():
        image_column, text_column = st.columns((1, 2))


    with text_column:
        st.subheader("DAY IN THE LIFE OF A CIVIL ENGINEER IN US (PINOY)")
        st.write(
            "In this video, I will share my typical day in the life as a Construction Civil Engineer (Office Edition) in America. By the way, I'm a Filipino Engineering Graduate who migrated in US last 2015.")
        st.markdown("[Watch the Video >](https://youtu.be/T_eVkOoLFAk)")

    with st.container():
        image_column, text_column = st.columns((1, 2))


    with text_column:
        st.subheader("A Day in the Life of a Civil Engineer | OFFICE Edition")
        st.write(
            "After a long period of working from home, I'm excited to document a day in my life as a City Traffic Engineer in the office. Traffic engineering is a sub-discipline of civil engineering")
        st.markdown("[Watch the Video >](https://youtu.be/qCZQj9TWCw4)")

    with st.container():
        image_column, text_column = st.columns((1, 2))


    with text_column:
        st.subheader("What Is Civil Engineering? (Is A Civil Engineering Degree Worth It?)")
        st.write(
            "These videos are for entertainment purposes only and they are just Shane's opinion based off of his own life experience and the research that he's done. ")
        st.markdown("[Watch the Video >](https://youtu.be/tBs57XfMPMI)")

if selected== "Contacts":
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = ("https://assets7.lottiefiles.com/packages/lf20_eroqjb7w.json")
    lottie_json = load_lottieurl(lottie_hello)
    st_lottie(lottie_json)

    st.header("Please Contact Us If You Have Any Concern")
    st.subheader("Princess Ann J. Catibog")
    st.write ("Contact Number: 09708276902")
    st.write("Email: catibogprincessann@gmail.com")
    st.write("-------------------------------------")
    st.subheader("Vince Aeron C. Estrada")
    st.write("Contact Number: 09506454136")
    st.write("Email: jeroestrada0731@gmail.com")
    st.write("-------------------------------------")
    st.subheader("Rainiel E. Reyes")
    st.write("Contact Number: 09304383268")
    st.write("Email: rainielreyes066@gmail.com")
    st.write("-------------------------------------")
    st.subheader("Meynard V. Villela")
    st.write("Contact Number:09158692340 ")
    st.write("Email: meynardvillela22@gmail.com")