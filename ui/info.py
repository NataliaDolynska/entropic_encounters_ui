ROLES = {
    'explorer': {'name': 'Explorer',
                 'image': 'roles/explorer.png',
                 'redirect': 'planet_selection',
                 'description': "Embark on a journey to distant worlds to learn from innovative societies. Gather insights to address Earth's pressing challenges."
                 },

    'celestial_citizen': {'name': 'Celestial Citizen',
                          'image': 'roles/celestial.png',
                          'redirect': 'society_selection',
                          'description': "Represent an advanced society shaped by overcoming adversity. Share your culture, values, and solutions to inspire Earth's future."
                          },
}

PLANETS = {
    "aridara": {'name': 'Aridara',
                'image_small': 'planets/aridara_small.jpg',
                'image_large': 'planets/full/aridara.jpg',
                'redirect': '/planet-description',
                'short_description': "A desert world where its inhabitants have mastered survival in extreme heat and scarcity.",
                'planet_brief': "Aridara is a vast desert planet defined by its scorching heat and endless dunes of red and orange sand. Life here has evolved to endure extreme conditions, where water is scarce and survival is a constant challenge.",
                'planetary_information_sheet': {
                    'environment': [
                        'Average Temperature: Daytime 45-55°C (113-131°F), nighttime 20-30°C (68-86°F)',
                        'Precipitation: 20-50 mm (0.8-2 inches) annually, infrequent but intense',
                        'Atmosphere: Thin, low humidity, primarily nitrogen and oxygen with elevated CO2 levels'
                        'Solar Radiation: Extreme, with minimal atmospheric protection',
                        'Wind Patterns: Frequent moderate winds, occasional severe dust storms'
                    ],
                    'ecosystems': [
                        'Flora: Highly drought-resistant plants, including deep-rooted shrubs and water-storing succulents',
                        'Fauna: Primarily small, burrowing animals and insects',
                        'Water Sources: Rare oases, deep aquifers'
                    ],
                    'natural_resources': [
                        "Water: Extremely scarce, primarily from deep underground sources",
                        "Energy: Abundant solar energy potential"
                    ]
                },
                'scientific_background': "The climate scenario for Aridara is based on projections for arid regions on Earth, particularly the expansion and intensification of deserts in North Africa, the Middle East, and parts of Central Asia by 2100. According to the Intergovernmental Panel on Climate Change (IPCC), under high-emission scenarios, global temperatures could rise by 3.3 to 5.7°C by the end of this century. This warming trend is expected to be more pronounced in arid regions, with some areas potentially experiencing temperature increases of up to 6°C above pre-industrial levels by 2100. The intensification of the global water cycle due to climate change is projected to increase the frequency and severity of droughts in many regions. Arid areas are particularly vulnerable, with annual precipitation expected to decrease by up to 30% in some desert regions by 2100. This reduction in rainfall, combined with increased evaporation rates due to higher temperatures, is likely to exacerbate water scarcity issues. Climate models also predict an increase in the frequency and intensity of extreme weather events, including heat waves and dust storms in arid regions. The expansion of desert areas, known as desertification, is expected to continue, potentially affecting up to 50% more land area by 2050 compared to 2000. These changes will have significant impacts on ecosystems, with many plant and animal species facing increased risk of extinction due to habitat loss and extreme conditions. However, some desert-adapted species may expand their ranges as arid conditions spread to new areas."
                },
    "hydros": {'name': 'Hydros',
               'image_small': 'planets/hydros_small.jpg',
               'image_large': 'planets/full/hydros.jpg',
               'redirect': '/planet-description',
               'short_description': "A water-covered planet with floating cities, where life thrives in harmony with the ocean’s depths.",
               'planet_brief': "Hydros is a planet almost entirely covered by water, where floating cities and underwater habitats have become the norm. Its inhabitants have developed a deep connection with the water, mastering the art of living in harmony with their aquatic environment. Advanced technologies allow them to harness the ocean’s resources sustainably while protecting the delicate marine ecosystems.",
               'planetary_information_sheet': {
                   'environment': [
                       'Average Temperature: 26-32°C (79-90°F), with minimal seasonal variation',
                       'Precipitation: Frequent rainfall (>2000 mm annually), intense tropical storms',
                       'Atmosphere: Highly humid, primarily nitrogen and oxygen with elevated CO2 levels'
                       'Wind Patterns: Strong trade winds, frequent hurricanes',
                   ],
                   'ecosystems': [
                       'Flora: Predominantly marine, including extensive kelp forests and floating vegetation',
                       'Fauna: Diverse marine life, some amphibious species on scattered land masses',
                       'Habitats: Floating settlements, underwater structures, and small natural islands'
                   ],
                   'natural_resources': [
                       "Water: Abundant seawater, desalination technology crucial",
                       "Energy: Wave, tidal, and geothermal energy sources"
                   ]

               },
               'scientific_background': "The climate scenario for Hydros is based on projections for coastal and island regions on Earth, particularly the impacts of sea-level rise, increased ocean temperatures, and changing weather patterns by 2100. According to the Intergovernmental Panel on Climate Change (IPCC), under high-emission scenarios, global mean sea level could rise by 0.61-1.10 meters by 2100, with some studies suggesting even higher figures. Ocean warming is expected to continue, with the upper ocean (0-700 m) projected to warm by 2°C to 4°C by 2100 under a high-emission scenario. This warming leads to increased stratification, reduced ocean oxygen content, and significant changes in marine ecosystems. The frequency and intensity of marine heatwaves are projected to increase substantially, potentially occurring 20 times more often by 2100 compared to pre-industrial levels. Climate models predict an intensification of the global water cycle, leading to more frequent and intense precipitation events in many regions. Tropical cyclones are expected to become more intense, with higher peak wind speeds and increased heavy precipitation. The El Niño Southern Oscillation (ENSO) and its impacts are projected to intensify, affecting global weather patterns. Sea-level rise will have profound impacts on coastal ecosystems and human settlements. By 2050, up to $106 billion worth of coastal property in the United States alone could be below sea level. Globally, millions of people are expected to be displaced due to rising seas and increased flooding events. These changes will significantly alter marine ecosystems. Ocean acidification, combined with warming and deoxygenation, is expected to negatively impact many marine species and ecosystems, particularly coral reefs. However, some species may expand their ranges as waters warm, leading to shifts in global marine biodiversity patterns."
               },
    "tempestia": {'name': 'Tempestia',
                  'image_small': 'planets/tempestia_small.jpg',
                  'image_large': 'planets/full/tempestia.jpg',
                  'redirect': '/planet-description',
                  'short_description': "A storm-ravaged planet where its resilient society has adapted to constant, violent weather conditions.",
                  'planet_brief': "Tempestia is a planet plagued by relentless storms, with violent winds and torrential rains shaping its rugged landscape. The inhabitants of Tempestia have adapted to this volatile environment by constructing resilient cities and developing technologies that harness the planet’s fierce weather to power their civilization.",
                  'planetary_information_sheet': {
                      'environment': [
                          'Climate Change Projection: Dominated by extreme weather due to atmospheric instability; constant storms with rapid temperature swings',
                          'Precipitation: Highly variable; torrential rains followed by dry spells; flash floods and droughts common',
                          'Atmosphere: Thick and turbulent, high water vapor content, frequent pressure and temperature fluctuations'
                          'Wind Patterns: Strong, unpredictable winds, hazardous for travel and construction',
                      ],
                      'ecosystems': [
                          'Flora: Hardy, fast-growing plants with deep roots; adapted to drought and rapid growth during wet periods',
                          'Fauna: Resilient species, many burrowing or with protective exoskeletons',
                          'Water Sources: Abundant but unstable; rivers and lakes change rapidly'
                      ],
                      'natural_resources': [
                          "Energy: Wind and storm energy harnessed with advanced technologies; geothermal energy from beneath the surface",
                          "Minerals: Rich mineral veins exposed by weather, mining is significant but dangerous"
                      ]
                  },
                  'scientific_background': "The climate scenario for Tempestia is inspired by projections for regions on Earth experiencing increased frequency and intensity of extreme weather events due to climate change. According to the Intergovernmental Panel on Climate Change (IPCC), global warming is expected to increase the intensity and frequency of extreme weather events,including hurricanes, tornadoes, and severe thunderstorms, by the end of this century. As global temperatures rise, the atmosphere holds more moisture, leading to more intense precipitation events. This can result in localized flash floods, even in areas that experience prolonged dry spells. The variability in precipitation patterns is projected to increase, with some regions facing more frequent and severe droughts while others encounter heavier rainfall. Climate models indicate that the frequency of intense tropical cyclones may increase, with a greater proportion reaching higher intensity levels. The warming of ocean surfaces is a key driver of this trend, providing more energy to fuel these storms. Additionally, the jet stream, which influences weather patterns, is expected to become more erratic due to Arctic warming, leading to more unpredictable wind patterns and storm tracks. These extreme weather patterns will have significant impacts on ecosystems and human infrastructure. Vegetation and wildlife will need to adapt to rapidly changing conditions, with species that can withstand both droughts and floods having a survival advantage. Human settlements and industries will need to develop resilient technologiesto harness the energy of these storms and protect against their destructive power."
                  }
}

SOCIETIES = {
    "aequorans": {
        'name': 'Aequorans',
        'short_description': 'The Aequorans originate from mobility-impaired individuals, now thriving in a society built around accessibility and adaptability.',
        'description': "The Aequorans are a species that evolved from individuals on Earth who faced mobility impairments. On their new planet, they have developed a society where accessibility and adaptability are central to daily life. Their physical forms have adapted to thrive in various environments, emphasizing fluid movement and resilience. The Aequorans value inclusivity, ensuring that all members of their society can contribute meaningfully. They have developed advanced technologies to overcome environmental challenges, creating a community where diversity is celebrated, and everyone’s abilities are harnessed for the greater good.",
        'image': 'society/aequorans_small.jpg',
        'redirect': '/society-description',
        'fact_sheet': {
            "Origin": "Mobility-impaired individuals from Earth.",
            "Planet": "Aridara, Hydros, Tempestia.",
            "Physical Traits": "Adaptive bodies with features optimized for mobility in harsh environments.",
            "Societal Values": "Accessibility, inclusivity, and resilience.",
            "Technologies": "Advanced mobility aids, sustainable infrastructure, and resource management systems.",
            "Social Structure": "Collaborative, with a focus on mutual support and ensuring equal participation.",
            "Cultural Practices": "Celebrations of diverse abilities, communal problem-solving, and innovative adaptation to environmental challenges.",
            "Challenges Overcome": "Overcame physical barriers to create an inclusive, thriving society.",
        },
        'challenges': {
            'earth': {
                "Mobility Barriers": "Faced physical and societal barriers due to environments not designed for mobility-impaired individuals.",
                "Lack of Accessibility": "Struggled with limited access to public spaces, transportation, and technologies that were not inclusive.",
                "Social Exclusion": "Experienced social isolation and marginalization due to their physical limitations.",
                "Limited Opportunities": "Had fewer opportunities in education, employment, and social participation due to systemic inaccessibility."
            },
            'new_planet': {
                "Universal Design": "Developed environments and technologies that are fully accessible to all, regardless of physical ability.",
                "Inclusive Infrastructure": "Built cities and communities with accessibility as a foundational principle, ensuring everyone can participate equally.",
                "Social Integration": "Established a culture that values and includes all individuals, fostering a strong sense of community and belonging.",
                "Empowerment Through Innovation": "Leveraged technological advancements to enhance mobility and independence, enabling full participation in society."
            }

        }
    },
    "ventari": {
        'name': 'Ventari',
        'short_description': 'The Ventari originate from nomadic and displaced peoples, creating a resilient society focused on mobility and flexibility.',
        'description': "The Ventari are a species that originated from nomadic and displaced peoples on Earth. They have built a society that thrives on mobility, flexibility, and a deep connection to the environment. Their culture is rooted in sustainable living, with an emphasis on resourcefulness and adaptability. The Ventari have developed advanced methods for managing resources and social organization, allowing them to prosper despite constant movement and environmental challenges. They value wisdom and cooperation, drawing on their history of overcoming adversity to build a resilient and sustainable community.",
        'image': 'society/ventari_small.jpg',
        'redirect': '/society-description',
        'fact_sheet': {
            "Origin": "Nomadic and displaced peoples from Earth.",
            "Planet": "Aridara, Hydros, Tempestia.",
            "Physical Traits": "Agile bodies adapted for movement across diverse terrains.",
            "Societal Values": "Mobility, sustainability, and adaptability.",
            "Technologies": "Resource management systems, portable infrastructure, and environmental adaptation techniques.",
            "Social Structure": "Flexible, with a focus on cooperation and collective decision-making.",
            "Cultural Practices": "Nomadic traditions, sustainable living practices, and communal resource sharing.",
            "Challenges Overcome": "Developed resilience and adaptability to thrive in constantly changing environments.",
        },
        'challenges': {
            'earth': {
                "Displacement": "Experienced displacement due to conflict, environmental degradation, or economic hardship.",
                "Social Instability": "Lived in unstable conditions with little access to permanent resources or security.",
                "Marginalization": "Faced social and cultural marginalization due to their nomadic lifestyle and lack of permanent residence.",
                "Resource Scarcity": "Struggled with limited access to essential resources like food, water, and shelter, often leading to survival challenges."
            },
            'new_planet': {
                "Sustainable Mobility": "Created a society where adaptability is a strength.",
                "Resilient Communities": "Built a flexible social structure that thrives on cooperation and resource sharing, ensuring stability despite constant movement.",
                "Cultural Respect": "Established a culture that honors each individual’s heritage, integrating it into the fabric of their society.",
                "Resource Abundance": "Developed advanced techniques for sustainable resource management, ensuring that all community members have access to essential needs."
            }

        }
    },
    "altracites": {
        'name': 'Altracites',
        'short_description': 'The Altracites descend from neurodivergent individuals, forming a society that celebrates cognitive diversity and innovative thinking.',
        'description': "The Altracites are a species descended from neurodivergent individuals on Earth. They have formed a society that values and leverages cognitive diversity, making innovative problem-solving a cornerstone of their culture. The Altracites possess heightened perceptual abilities, which they use to navigate and thrive in their complex environments. Their society is deeply collaborative, with a strong emphasis on intellectual diversity and unconventional thinking. They have developed unique technologies and social systems that reflect their diverse cognitive strengths, creating a community where every perspective is valued and integrated into the collective effort.",
        'image': 'society/altracites_small.jpg',
        'redirect': '/society-description',
        'fact_sheet': {
            "Origin": "Neurodivergent individuals from Earth.",
            "Planet": "Aridara, Hydros, Tempestia.",
            "Physical Traits": "Enhanced cognitive and perceptual abilities, with a focus on problem-solving.",
            "Societal Values": "Cognitive diversity, innovation, and collaboration.",
            "Technologies": "Adaptive technologies that harness cognitive strengths, advanced problem-solving tools, and communal decision-making systems.",
            "Social Structure": "Inclusive, with a focus on leveraging diverse perspectives and skills.",
            "Cultural Practices": "Celebrations of intellectual diversity, collective problem-solving, and innovative thinking.",
            "Challenges Overcome": "Created a society where diverse cognitive abilities are central to communal success and resilience.",
        },
        'challenges': {
            'earth': {
                "Misunderstanding and Stigma": "Faced misunderstanding, stigma, and marginalization due to their neurodivergent minds.",
                "Lack of Support": "Struggled with inadequate support systems that did not cater to their unique cognitive needs.",
                "Educational Barriers": "Encountered difficulties in traditional education systems that were not designed to accommodate diverse ways of thinking.",
                "Limited Employment Opportunities": "Had limited job prospects due to societal biases and a lack of recognition of their strengths.",
            },
            'new_planet': {
                "Celebration of Diversity": "Established a society that values and harnesses cognitive diversity, recognizing it as a key to innovation and problem-solving.",
                "Tailored Support Systems": "Developed support systems and technologies specifically designed to enhance their cognitive strengths and accommodate diverse needs.",
                "Inclusive Education": "Created an education system that embraces different learning styles, ensuring that everyone can achieve their full potential.",
                "Valued Contributions": "Built a society where all individuals, regardless of cognitive differences, can contribute meaningfully and are recognized for their unique strengths."}

        }
    },
}

OPENING_MONOLOGUES = {
    "aequorans_aridara": [
        """As you step onto the hot, shifting sands of Aridara, an Aequoran approaches you, moving with a fluid grace that defies the harsh environment. Its robust exoskeleton glistens under the relentless sun.""",
        "The Aequoran starts talking to you:",
        """
        "Welcome, travelers, to Aridara. I am one of the Aequorans, a species that
        has turned this arid world into a place where all can thrive. Our forefathers
        once lived on Earth, where they faced discrimination and exclusion because
        of their mobility impairments. They struggled in societies that were not
        designed for them. Many of them could not move or manage their daily life
        without help of other humans. As soon as the technology was ready, a
        couple of our courageous ancestors made the joint decision to leave planet
        Earth and become the founders of a new society. Here, on Aridara, we have
        created a world where accessibility is the norm. We have built a society that
        embraces diversity and turns challenges into strengths. On Earth, we were
        marginalized and often overlooked, but here, we are the architects of a world
        where everyone has a place, and no one is left behind."
        """
    ],

    "aequorans_hydros": [
        "As you step out onto the floating platform of Hydros, the gentle waves rocking beneath your feet, an Aequoran emerges from the water. It pulls itself onto the platform with fluid strength. The Aequoran’s technology-enhanced body is perfectly suited to the watery world around you.",
        "It regards you with a welcoming gaze.",
        """
        "Greetings, explorers, to Hydros. I am an Aequoran, part of a species that has
        embraced the ocean’s depths and its floating islands as our home. Our forefathers
        once lived on Earth, where they faced discrimination and exclusion because of their
        mobility impairments. They struggled in societies that were not designed for them.
        Many of them could not move or manage their daily life without help of other humans.
        As soon as the technology was ready, a couple of our courageous ancestors made the
        joint decision to leave planet Earth and become the founders of a new society. Here,
        on Hydros, we have created a world where accessibility is the norm. We have built a
        society that embraces diversity and turns challenges into strengths. On Earth, we
        were marginalized and often overlooked, but here, we are the architects of a world
        where everyone has a place, and no one is left behind."
        """
    ],

    "aequorans_tempestia": [
        "As you brace yourself against the fierce winds of Tempestia, an Aequoran approaches. The Aequoran’s looks as if no turbulent weather could put it at risk. It offers you a nod of acknowledgment, its presence radiating calm amid the chaos: It regards you with a welcoming gaze.",
        """
        "Welcome to Tempestia, travelers. I am an Aequoran, part of a species that has
        learned to thrive in the face of nature’s fury. Our forefathers once lived on Earth,
        where they faced discrimination and exclusion because of their mobility
        impairments. They struggled in societies that were not designed for them. Many of
        them could not move or manage their daily life without help of other humans.
        """,
        """
        As soon as the technology was ready, a couple of our courageous ancestors made
        the joint decision to leave planet Earth and become the founders of a new society.
        Here, on Tempestia, we have created a world where accessibility is the norm. We
        have built a society that embraces diversity and turns challenges into strengths. On
        Earth, we were marginalized and often overlooked, but here, we are the architects
        of a world where everyone has a place, and no one is left behind."
        """
    ],

    "ventari_aridara": [
        """As you arrive on the scorched surface of Aridara, a figure emerges from the horizon,
moving with practiced ease across the desert. A tall Ventari approaches you with a
calm, steady gait, its skin weathered by the harsh environment but its spirit clearly
unbroken:""",
        """
        "Welcome, travelers, to Aridara. I am one of the Ventari, a species that has mastered
        the art of survival in this unforgiving desert. Our ancestors once roamed the Earth as
        nomads, forced to move constantly due to conflicts and environmental changes.
        They were often displaced, their wisdom overlooked by more settled societies.
        """,
        """
        As soon as the technology was ready, a courageous group of our ancestors decided
        to leave Earth and become the founders of a new society. Here, on Aridara, we have
        turned our heritage into strength.
        """,
        """We move with the winds and the sands. On Earth, we were marginalized, our way of
        life misunderstood. But here, our nomadic roots have allowed us to build a society
        that is resilient, adaptable, and deeply connected to the land. We have learned that
        true survival comes from understanding and respecting the environment, not
        fighting against it."
        """
    ],
    "ventari_hydros": [
        """
As your ship docks against a floating village on Hydros, you see a Ventari skillfully
maneuvering a small vessel through the waves, moving with the ease of someone
who has spent a lifetime at sea. The Ventari hops onto the dock and approaches
you with a welcoming smile.
""",
        """
        "Greetings, explorers, to Hydros. I am one of the Ventari, a species born from the
        tides and currents of this oceanic world. Our ancestors once roamed the Earth as
        nomads, forced to move constantly due to conflicts and environmental changes.
        They were often displaced, their wisdom overlooked by more settled societies. As
        soon as the technology was ready, a courageous group of our ancestors decided to
        leave Earth and become the founders of a new society.
        """,
        """
        Here, on Hydros, our nomadic heritage has become our greatest asset. We have
        mastered the art of living with the ocean, moving our communities as the currents
        dictate, harvesting resources without depleting them, and finding harmony in
        constant change. On Earth, we were often seen as rootless, but here, our roots are
        deep within the waters that sustain us."
        """
    ],

    "ventari_tempestia": [
        """
Amidst the howling winds of Tempestia, you spot a figure navigating the storm with
effortless precision. The Ventari, cloaked against the elements, approaches with a
confident stride, its eyes scanning the sky and the land with an experienced gaze.
""",

        """
        "Welcome, travelers, to Tempestia. I am one of the Ventari, a species that has
        learned to live in harmony with this planet’s relentless weather conditions. Our
        ancestors once roamed the Earth as nomads, forced to move constantly due to
        conflicts and environmental changes. They were often displaced, their wisdom
        overlooked by more settled societies.
        """,
        """
        As soon as the technology was ready, a courageous group of our ancestors decided
        to leave Earth and become the founders of a new society. Here, on Tempestia, we
        have embraced our heritage. We adapt to the weather, not trying to fight it, finding
        safety in the chaos and strength in our adaptability.
        """,

        """
        On Earth, our ancestors were often outcasts, but here, we are the keepers of
        ancient wisdom, knowing how to navigate an ever-changing landscape. We have
        built a society that thrives in motion, teaching that sometimes the best way to
        survive is to keep moving, to stay flexible, and to never stop adapting."
        """
    ],

    "altracites_aridara": [

        """
        As you step onto the scorching sands of Aridara, the harsh sunlight casting long
        shadows, an Altracite approaches with deliberate, graceful movements. They give
        you a calm, measured nod as you meet.
        """,
        """
        "Welcome to Aridara, explorers. I am one of the Altracites, a species that has
        flourished on this unforgiving world through our ability to perceive and understand
        the environment in ways others cannot. Our ancestors once lived on Earth, where
        they were often misunderstood and marginalized due to their neurodivergent
        minds.
        """,
        """
        As soon as the technology was ready, a courageous group of our ancestors decided
        to leave Earth and become the founders of this new society. But here, on Aridara,
        we have built a society where our unique ways of thinking are celebrated and
        essential.
        """,
        """
        Our diverse cognitive abilities are valued while everybody’s preferences are
        respected. We have mastered a way to find community in diversity and harnessing
        everybody’s talents, leaving no one behind and proving that different perspectives
        are vital for survival."
        """
    ],

    "altracites_hydros": [
        """
As you step onto the floating platform on Hydros, you notice an Altracite standing at
the edge, gazing intently into the shimmering waters below. With a slow, deliberate
turn, the Altracite faces you, their expression both welcoming and contemplative.
""",
        """
        "Welcome to Aridara, explorers. I am one of the Altracites, a species that has
        flourished on this unforgiving world through our ability to perceive and understand
        the environment in ways others cannot.
        """,
        """
        Our ancestors once lived on Earth, where they were often misunderstood and
        marginalized due to their neurodivergent minds. As soon as the technology was
        ready, a courageous group of our ancestors decided to leave Earth and become the
        founders of this new society.
        """,
        """
        Here, on Hydros, our unique way of seeing the world has allowed us to thrive in
        harmony with the water. Our diverse cognitive abilities are valued while everybody’s
        preferences are respected. We have mastered a way to find community in diversity
        and harnessing everybody’s talents, leaving no one behind and proving that
        different perspectives are vital for survival."
        """
    ],

    "altracites_tempestia": [
        """As you struggle against the powerful winds of Tempestia, an Altracite appears
seemingly out of nowhere, their form stable and composed amidst the chaos. Their
large, multifaceted eyes scan the stormy horizon, taking in details invisible to the
naked eye. They approach you with measured steps, unaffected by the turbulent
environment.
""",
        """
        "Welcome to Tempestia, brave explorers. I am an Altracite, part of a species that
        has learned to see beyond the surface, to understand the deeper patterns in the
        chaos. Our ancestors once lived on Earth, where they were often overlooked
        because of their neurodivergent minds. They saw the world differently, and because
        of that, they were often excluded from the mainstream. But when the time came, a
        courageous group of our ancestors decided to leave Earth and become the
        founders of a new society.
        """,
        """
        Here, on Tempestia, our ability to perceive the hidden rhythms of the world has
        become our greatest strength. On Earth, we were often marginalized, but here, we
        are the guardians of resilience, using our unique abilities to protect and sustain our
        people in the face of Tempestia’s relentless fury."
        """
    ]

}

THOUGHT_PROMPTS = {

    'aequorans_aridara': {
        "Adaptive Infrastructure": "Consider how Aequorans might have designed their buildings and public spaces to maximize accessibility despite the harsh desert environment, using technologies that protect against heat and sand.",
        "Social Integration": "Reflect on how they’ve fostered a culture of mutual support, where the physical challenges of living in such a harsh environment are mitigated by strong communal bonds.",
        "Environmental Solutions": "Consider how they might harness solar energy efficiently, using it not only for power but also to create cooler environments in their homes and communal spaces."
    },

    'aequorans_hydros': {
        "Amphibious Mobility": "Think about how they’ve developed adaptive technology that allows them to move effortlessly between land and water, integrating swimming or aquatic mobility into their daily lives.",
        "Disaster Preparedness": "Consider how they’ve built resilience against water disasters (e.g., floods, tsunamis) with technologies that protect their floating habitats and ensure safety for all.",
        "Social Integration": "Reflect on how they’ve fostered a culture of mutual support, where the physical challenges of living in such a harsh environment are mitigated by strong communal bonds."
    },

    'aequorans_tempestia': {
        "Mobility in Storms": "Consider how they’ve adapted their mobility aids to ensure safe and effective movement even in the midst of extree weather, such as powerful winds and heavy rains.",
        "Emergency Response": "Reflect on how they’ve developed rapid response systems that ensure the safety and well-being of all citizens during sudden and severe weather changes.",
        "Resilience Culture": "Imagine how their society celebrates resilience and adaptability, fostering a strong communal spirit that supports all members.",
        "Social Integration": "Reflect on how they’ve fostered a culture of mutual support, where the physical challenges of living in such a harsh environment are mitigated by strong communal bonds."
    },

    'ventari_aridara': {
        "Nomadic Adaptation": "Imagine how the Ventari have created portable and modular living spaces that can be easily assembled and disassembled as they move across the desert.",
        "Cultural Preservation": "Consider how they’ve maintained their traditions, using storytelling and rituals to pass down wisdom from generation to generation.",
        "Community Networks": "Visualize how they’ve built a strong network of interconnected communities, ensuring that everyone has access to the support and resources they need while on the move."
    },

    'ventari_hydros': {
        "Floating Villages": "Envision how the Ventari have created mobile, floating villages that drift with the ocean currents, allowing them to follow resource flows and avoid harsh weather.",
        "Fluid Social Structures": "Reflect on how their society’s social structure is as fluid as the water they live on, with flexible roles and responsibilities that change based on environmental needs.",
        "Cultural Integration": "Imagine how they’ve blended their heritage with a deep respect for the environment, creating a unique culture that celebrates both movement and marine life."
    },

    'ventari_tempestia': {
        "Mobile Shelters": "Visualize how the Ventari have designed shelters that can be quickly packed and relocated in response to Tempestia’s unpredictable storms.",
        "Resilient Communities": "Reflect on how their communities are designed to be flexible and resilient, with structures that can withstand or adapt to extreme weather conditions.",
        "Emergency Mobility": "Think about how they’ve developed rapid mobility solutions, ensuring that everyone in their community can evacuate or relocate quickly when needed.",
        "Community Networks": "Visualize how they’ve built a strong network of interconnected communities, ensuring that everyone has access to the support and resources they need while on the move."
    },
    "altracites_aridara": {
        "Cognitive Collaboration": "Consider how their society uses diverse cognitive abilities to solve complex environmental challenges, such as extreme heat and resource scarcity.",
        "Knowledge Sharing": "Think about how they’ve built a culture of continuous learning and adaptation, where everyone’s ideas are valued and contribute to the community’s survival.",
        "Innovative Architecture": "Imagine how they’ve designed their buildings and infrastructure to not only withstand the heat but also enhance the well-being of all citizens, making use of reflective materials and underground spaces."
    },
    "altracites_hydros": {
        "Fluid Thought": "Reflect on how their society’s approach to problem-solving is as fluid and adaptable as the water around them, allowing them to quickly adjust to changing oceanic conditions.",
        "Symbiotic Living": "Envision how they’ve created a symbiotic relationship with nature, using their perceptual strengths to understand and work with marine ecosystems rather than against them.",
        "Cognitive Harmony": "Think about how they’ve built a society where different cognitive perspectives are not just accepted but celebrated, leading to innovations in communal living and resource management."
    },
    "altracites_tempestia": {
        "Fluid Thought": "Reflect on how their society’s approach to problem-solving is as diverse and multi-faceted as the weather around them, allowing them to quickly adjust to changing conditions.",
        "Collaborative Innovation": "Reflect on how their society’s emphasis on cognitive diversity has led to innovative solutions for harnessing the environmental conditions and ensuring community safety.",
        "Cultural Resilience": "Think about how they’ve integrated the concept of resilience into their cultural practices, using their unique insights to turn Tempestia’s challenges into opportunities for growth.",
        "Adaptive Learning": "Imagine how they’ve built an educational system that continuously adapts to the changing environment, ensuring that every citizen is prepared to contribute to the community’s survival and success."
    }
}


QUESTION_CATEGORIES = {
    "Society and Culture": {
        'image': 'questions/society.png',
        'description': "Explore how the society values inclusivity, diversity, and shared traditions.",
        'questions': [
            "How have you structured your society to ensure that everyone feels included and valued?",
            "What are the core values that guide your community? How did these values evolve over time?",
            "How do you celebrate diversity within your community? What practices ensure that all voices are heard?"
        ]},
    "Technology and Innovation": {
        'image': 'questions/technology.png',
        "description": "Discover how innovation shapes life and addresses challenges.",
        'questions': [
            "What technological innovations have been most crucial in adapting to your environment?",
            "How do you ensure that new technologies are accessible to everyone in your society?",
            "Can you share an example of how your society overcame a major challenge through innovation and collaboration?"
        ]},
    "Environment and Sustainability": {
        'image': 'questions/environment.png',
        "description": "Learn how the society lives in harmony with its environment.",
        'questions': [
            "How have you managed to live in harmony with your environment?",
            "What strategies do you use to ensure the long-term sustainability of your resources?",
            "How do you teach future generations to respect and care for the environment?"
        ]},
    "Economy and Cooperation": {
        'image': 'questions/economy.png',
        "description": "Understand how collaboration and fairness support the community.",
        'questions': [
            "What does cooperation look like in your society?",
            "How do you handle disagreements or conflicts?",
            "How do you ensure that the most vulnerable members of your society are supported and empowered?",
            "How do you balance individual needs with the needs of the community?"
        ]
    }

}
