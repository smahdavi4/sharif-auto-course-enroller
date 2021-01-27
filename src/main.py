from captcha.solver import solve_captcha, load_captcha_data

example_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="150" height="50" viewBox="0,0,150,50"><path d="M12 12 C89 40,90 47,143 40" stroke="#666" fill="none"/><path fill="#333" d="M53.55 40.29L53.61 40.35L53.74 40.48Q49.55 40.59 48.56 38.27L48.64 38.34L48.64 38.35Q49.30 37.30 50.86 35.51L50.84 35.49L50.92 35.56Q51.41 37.58 54.42 37.69L54.42 37.70L54.37 37.64Q57.80 37.77 59.44 36.43L59.36 36.35L59.47 36.47Q60.84 34.83 60.77 32.13L60.76 32.12L60.68 32.04Q60.70 27.15 55.91 27.38L55.86 27.33L55.86 27.33Q52.98 27.42 51.23 28.68L51.28 28.73L50.90 28.50L50.75 28.42L50.66 28.33Q51.13 25.30 51.02 22.56L50.96 22.51L50.92 22.47Q50.80 19.84 50.46 16.53L50.44 16.50L50.45 16.52Q54.06 17.43 57.87 17.31L57.89 17.33L58.01 17.46Q61.73 17.29 65.31 16.03L65.30 16.02L64.85 17.66L64.67 17.49Q64.45 18.34 64.26 19.18L64.27 19.18L64.18 19.09Q61.23 20.29 57.35 20.29L57.28 20.23L57.18 20.13Q55.74 20.13 54.26 19.98L54.29 20.01L54.34 20.06Q54.31 20.80 53.97 25.25L53.92 25.20L53.90 25.18Q54.74 24.72 56.79 24.57L56.84 24.62L56.80 24.58Q60.49 24.77 61.94 26.45L62.00 26.51L61.90 26.40Q63.35 28.00 63.61 31.85L63.52 31.76L63.69 31.93Q63.93 36.09 62.72 38.11L62.65 38.04L62.67 38.06Q60.73 40.05 57.42 40.28L57.33 40.18L57.31 40.16Q56.33 40.25 53.66 40.40ZM59.63 42.59L59.68 42.65L59.69 42.66Q63.03 42.65 64.94 41.55L64.97 41.58L64.98 41.59Q66.10 40.20 66.10 38.11L66.03 38.03L66.03 38.03Q66.04 34.97 65.09 30.85L65.10 30.86L64.99 30.75Q64.77 29.16 63.55 27.75L63.48 27.68L63.47 27.71L63.29 27.46L62.89 27.21L62.86 27.17Q62.66 26.56 62.02 25.87L62.04 25.89L62.05 25.94L62.01 25.91Q60.48 24.22 56.79 24.22L56.68 24.11L56.50 24.20L56.42 24.13Q56.65 23.70 56.84 22.60L56.82 22.58L56.77 22.54Q61.67 22.56 65.70 20.92L65.74 20.96L65.84 21.06Q66.26 19.65 67.21 16.83L67.18 16.80L65.11 17.77L65.08 17.75Q65.35 16.50 65.85 15.35L65.86 15.36L65.88 15.38Q62.12 16.92 58.01 17.00L58.05 17.04L57.90 16.89Q53.88 17.09 49.92 15.99L49.82 15.88L49.97 16.03Q50.56 20.36 50.56 24.77L50.59 24.81L50.59 24.80Q50.61 26.72 50.49 28.63L50.48 28.61L50.45 28.58Q50.75 28.81 51.32 29.11L51.23 29.02L51.33 29.13Q51.58 28.80 52.22 28.45L52.28 28.51L52.34 28.57Q52.33 29.36 52.10 30.88L51.99 30.77L51.98 30.77Q52.50 31.05 52.92 31.28L52.96 31.32L52.97 31.33Q55.62 29.46 57.49 29.46L57.59 29.55L57.53 29.50Q58.78 29.42 59.96 30.07L60.06 30.16L60.07 30.17Q60.36 31.15 60.40 32.10L60.41 32.12L60.39 32.09Q60.59 34.80 59.56 35.91L59.49 35.83L59.51 35.85Q58.01 36.94 55.76 37.17L55.88 37.29L55.86 37.26Q54.80 37.24 54.11 37.16L54.19 37.23L54.17 37.21Q53.44 37.21 52.68 36.86L52.51 36.70L52.65 36.65L52.51 36.73L52.43 36.66Q51.60 36.13 51.07 34.80L51.14 34.88L51.04 34.77Q49.79 36.26 48.12 38.39L48.18 38.46L48.05 38.33Q48.38 39.00 49.22 39.96L49.19 39.92L49.35 40.09Q50.26 41.76 53.08 42.25L53.10 42.28L53.16 42.34Q54.32 42.54 59.69 42.66Z"/><path fill="#333" d="M26.61 29.11L26.71 29.21L26.57 29.07Q24.80 29.01 23.56 30.44L23.56 30.44L23.64 30.51Q22.24 31.78 22.05 33.68L22.14 33.78L22.04 33.68Q21.83 35.75 22.92 36.72L22.91 36.72L22.93 36.73Q24.11 37.80 26.21 37.69L26.21 37.70L26.07 37.55Q28.20 37.44 29.31 36.75L29.32 36.77L29.40 36.85Q30.52 35.72 30.52 34.16L30.47 34.12L30.58 34.22Q30.43 33.69 30.36 33.31L30.46 33.41L30.34 33.30Q30.41 31.62 29.31 30.27L29.37 30.33L29.38 30.34Q28.21 28.92 26.53 29.03ZM26.18 40.21L26.14 40.17L26.12 40.15Q21.76 40.17 20.35 39.41L20.33 39.39L20.45 39.51Q19.29 38.62 19.10 36.91L19.24 37.04L19.09 36.90Q19.22 36.38 19.26 35.66L19.10 35.49L19.27 35.66Q19.28 34.57 19.28 34.11L19.26 34.09L19.38 34.21Q19.78 31.30 19.93 30.62L19.98 30.66L19.92 30.61Q20.45 28.74 21.29 27.33L21.26 27.30L21.27 27.31Q23.96 22.96 29.90 16.60L29.73 16.43L29.85 16.55Q32.50 16.23 34.71 15.43L34.66 15.39L34.64 15.37Q27.91 22.94 24.71 27.17L24.62 27.08L24.58 27.04Q25.68 26.66 26.97 26.66L26.92 26.60L26.86 26.54Q30.30 26.68 31.83 28.62L31.74 28.53L31.77 28.56Q33.17 30.26 33.51 33.80L33.41 33.70L33.42 33.72Q33.49 34.42 33.49 35.03L33.53 35.07L33.43 34.98Q33.51 38.18 31.30 39.24L31.21 39.15L31.19 39.14Q30.00 39.77 26.12 40.15ZM28.40 42.55L28.43 42.58L28.44 42.59Q29.69 42.50 31.67 42.58L31.76 42.67L31.80 42.71Q33.36 42.72 34.92 41.99L34.88 41.95L34.86 41.93Q36.15 41.31 36.15 39.52L36.04 39.41L36.08 39.46Q35.96 38.84 35.79 37.85L35.88 37.94L35.79 37.85Q35.74 36.99 35.74 36.53L35.73 36.52L35.78 36.57Q34.76 31.70 33.16 29.80L33.20 29.84L33.14 29.78Q33.12 29.72 32.97 29.49L32.95 29.47L32.61 29.21L32.68 29.32L32.65 29.28Q32.26 28.74 31.65 27.79L31.68 27.82L31.62 27.76Q30.67 26.77 28.69 26.32L28.81 26.44L28.73 26.36Q30.07 24.88 33.04 21.19L32.89 21.04L37.18 15.81L37.19 15.82Q35.72 16.79 33.33 17.55L33.25 17.48L33.20 17.42Q34.22 16.55 36.01 14.57L35.85 14.40L36.03 14.58Q33.59 15.61 29.71 16.18L29.76 16.23L29.71 16.18Q24.00 22.08 21.03 27.03L21.07 27.07L20.91 26.92Q19.55 29.59 18.98 35.83L18.89 35.75L18.85 35.70Q18.86 36.36 18.93 37.31L18.84 37.22L18.79 37.16Q18.97 39.02 20.07 39.93L20.05 39.91L20.12 39.98Q20.38 40.01 20.35 40.05L20.36 40.06L20.44 40.15Q20.88 41.12 21.68 41.54L21.60 41.46L21.53 41.39Q22.99 42.09 24.93 42.28L24.93 42.27L24.92 42.27Q24.89 42.24 28.39 42.54ZM28.33 31.48L28.20 31.35L28.22 31.36Q28.74 31.20 29.69 31.70L29.86 31.87L29.76 31.77Q30.17 32.78 30.17 33.43L30.20 33.46L30.07 33.34Q30.35 35.29 29.40 36.28L29.37 36.24L29.31 36.19Q28.24 36.91 26.15 37.22L26.11 37.18L26.27 37.34Q24.82 37.33 24.29 37.07L24.23 37.00L24.18 36.96Q24.04 36.55 24.04 36.24L24.12 36.33L24.08 36.29Q23.76 32.92 26.69 31.63L26.73 31.67L26.76 31.69Q27.57 31.40 28.33 31.48Z"/><path fill="#444" d="M82.66 40.41L82.52 40.27L82.69 40.43Q81.27 40.50 79.71 40.09L79.69 40.06L79.54 39.92Q78.42 39.10 78.26 37.46L78.30 37.49L78.32 37.52Q78.24 37.29 78.44 34.66L78.31 34.54L78.34 34.56Q79.51 34.52 81.53 34.14L81.36 33.97L81.34 34.90L81.20 34.76Q80.91 36.49 82.32 37.06L82.45 37.19L82.31 37.05Q83.23 37.51 85.32 37.51L85.23 37.42L85.25 37.44Q86.97 37.41 87.16 37.33L87.15 37.32L87.17 37.34Q88.09 37.19 88.81 36.70L88.79 36.68L88.79 36.68Q90.17 35.69 89.97 33.60L89.95 33.58L89.88 33.50Q89.72 31.10 87.99 29.54L88.11 29.66L87.96 29.51Q86.29 28.01 83.81 28.01L83.88 28.07L83.83 27.79L83.74 27.71Q84.16 27.71 85.04 27.64L85.07 27.66L85.11 27.71Q86.98 27.55 88.35 26.32L88.31 26.29L88.35 26.32Q89.78 25.14 89.93 23.27L89.85 23.19L89.96 23.30Q89.98 22.91 89.98 22.57L89.88 22.46L89.91 22.49Q89.97 21.03 88.60 20.12L88.64 20.15L88.66 20.18Q87.29 19.23 85.70 19.34L85.83 19.48L85.77 19.42Q84.38 19.17 83.16 19.59L83.31 19.73L83.22 19.65Q81.79 20.19 81.48 21.34L81.48 21.33L81.49 21.34Q81.26 22.06 81.33 22.82L81.44 22.93L81.42 22.91Q80.37 22.66 78.31 21.94L78.32 21.94L78.26 21.89Q78.04 20.21 78.07 19.37L78.07 19.37L78.02 19.32Q78.17 17.83 79.23 17.15L79.29 17.20L79.19 17.10Q80.69 16.58 82.29 16.58L82.19 16.49L82.36 16.65Q85.37 16.47 88.53 16.74L88.66 16.87L88.59 16.80Q93.65 17.21 93.34 20.98L93.33 20.96L93.38 21.01Q93.31 22.51 92.82 24.07L92.86 24.11L92.77 24.02Q91.81 27.06 89.45 27.98L89.47 27.99L89.53 28.05Q92.10 28.53 92.71 31.88L92.83 32.00L92.82 31.99Q93.06 33.14 93.13 35.16L92.97 35.00L92.97 35.00Q93.26 39.59 88.66 40.05L88.58 39.97L88.67 40.06Q87.93 40.12 82.64 40.39ZM87.73 42.51L87.84 42.62L87.81 42.58Q88.37 42.57 91.22 42.65L91.33 42.75L91.35 42.78Q92.97 42.72 94.60 42.07L94.59 42.06L94.65 42.12Q95.90 41.24 95.71 39.49L95.64 39.42L95.63 39.41Q95.59 38.14 95.28 36.39L95.27 36.38L95.19 36.30Q94.58 31.92 92.64 30.28L92.57 30.22L92.40 29.85L92.28 29.69L92.26 29.68Q94.09 28.31 94.86 23.94L94.95 24.03L94.78 23.86Q94.98 23.57 95.10 22.62L95.07 22.59L95.08 22.60Q95.16 21.84 95.08 21.16L95.03 21.10L95.06 21.13Q94.91 19.46 93.62 18.78L93.48 18.64L93.43 18.66L93.39 18.63Q93.12 17.67 91.98 17.14L91.94 17.10L92.10 17.26Q90.48 16.48 85.34 16.17L85.47 16.30L85.45 16.28Q83.78 16.21 82.18 16.21L82.11 16.14L82.09 16.12Q80.54 16.17 79.02 16.82L79.05 16.85L79.01 16.80Q77.81 17.59 77.81 19.34L77.70 19.23L77.77 19.30Q77.83 18.94 78.10 22.29L77.97 22.16L78.04 22.24Q78.33 22.29 79.96 22.90L80.01 22.95L79.96 22.90Q80.00 23.47 79.96 23.96L79.88 23.89L79.91 23.91Q79.93 24.43 79.97 24.96L79.87 24.87L80.04 25.03Q81.83 25.42 83.85 25.53L83.72 25.40L83.78 25.46Q83.63 23.37 84.73 22.53L84.87 22.67L84.88 22.68Q85.64 21.96 87.66 21.73L87.59 21.65L87.68 21.75Q88.85 21.77 89.42 21.96L89.39 21.94L89.45 22.00Q89.37 21.99 89.40 22.10L89.42 22.12L89.41 22.30L89.46 22.81L89.54 22.88Q89.47 23.01 89.43 23.16L89.50 23.22L89.59 23.32Q89.47 24.99 87.95 26.17L87.83 26.05L87.98 26.20Q86.98 27.03 84.96 27.22L85.02 27.28L85.08 27.33Q84.36 27.48 83.48 27.48L83.38 27.39L83.30 27.31Q83.42 27.73 83.57 28.42L83.50 28.34L83.57 28.42Q85.29 28.38 86.74 29.10L86.70 29.07L86.68 29.16L85.14 29.37L85.17 29.41Q85.22 29.75 85.33 30.36L85.25 30.28L85.31 30.35Q87.44 30.26 89.15 31.59L89.01 31.46L89.16 31.61Q89.41 32.01 89.71 33.64L89.56 33.49L89.56 33.49Q89.82 36.49 86.89 36.90L86.81 36.83L86.85 36.87Q84.83 37.21 84.26 37.17L84.29 37.20L84.26 37.17Q83.81 37.07 83.28 36.99L83.28 36.99L83.28 36.54L83.32 36.00L83.48 35.75L83.47 35.40L83.34 35.27Q82.39 35.34 81.59 35.53L81.76 35.70L81.71 35.66Q81.74 35.49 81.74 35.30L81.55 35.11L81.70 35.26Q81.77 35.10 81.77 34.87L81.71 34.81L81.75 34.85Q81.81 34.46 81.96 33.73L81.79 33.56L81.86 33.63Q79.92 33.78 78.05 34.12L78.19 34.26L78.05 34.12Q78.04 34.61 77.93 35.73L78.05 35.86L78.08 35.88Q78.01 37.05 78.01 37.66L77.85 37.50L77.95 37.60Q77.98 39.61 79.35 40.37L79.31 40.33L79.36 40.38Q80.88 42.71 85.61 42.51L85.66 42.57L85.63 42.54Q86.23 42.38 87.75 42.53Z"/><path fill="#111" d="M112.87 40.41L112.86 40.39L112.83 40.37Q108.76 40.60 107.77 38.27L107.85 38.35L107.87 38.38Q108.49 37.28 110.05 35.49L110.19 35.63L110.18 35.62Q110.56 37.53 113.57 37.64L113.53 37.60L113.64 37.72Q116.90 37.67 118.54 36.33L118.65 36.44L118.56 36.35Q120.02 34.81 119.95 32.11L119.98 32.14L119.88 32.04Q119.87 27.11 115.07 27.34L115.02 27.29L114.95 27.23Q112.17 27.41 110.42 28.67L110.37 28.62L110.04 28.44L109.85 28.33L109.82 28.29Q110.29 25.27 110.18 22.53L110.07 22.42L110.08 22.43Q110.07 19.90 109.72 16.59L109.78 16.64L109.69 16.56Q113.39 17.56 117.20 17.44L117.05 17.30L117.13 17.37Q120.87 17.23 124.45 15.98L124.46 15.98L123.91 17.53L123.90 17.51Q123.73 18.42 123.54 19.26L123.54 19.25L123.43 19.15Q120.37 20.23 116.49 20.23L116.42 20.16L116.54 20.28Q114.94 20.14 113.46 19.98L113.49 20.02L113.56 20.09Q113.40 20.68 113.06 25.14L113.20 25.28L113.10 25.18Q113.92 24.71 115.98 24.56L115.95 24.52L116.04 24.62Q119.75 24.82 121.19 26.50L121.09 26.40L121.13 26.44Q122.54 28.00 122.81 31.84L122.86 31.90L122.85 31.88Q123.14 36.10 121.92 38.12L121.89 38.08L121.93 38.12Q119.87 39.99 116.56 40.22L116.62 40.27L116.55 40.21Q115.42 40.14 112.75 40.29ZM118.92 42.68L118.95 42.72L118.86 42.62Q122.40 42.82 124.30 41.72L124.26 41.68L124.25 41.66Q125.26 40.16 125.26 38.07L125.21 38.01L125.28 38.08Q125.18 34.90 124.23 30.79L124.35 30.91L124.18 30.74Q123.96 29.15 122.74 27.74L122.63 27.63L122.64 27.68L122.42 27.38L122.21 27.32L122.22 27.34Q121.91 26.61 121.26 25.92L121.27 25.93L121.12 25.82L121.16 25.86Q119.60 24.15 115.91 24.15L115.95 24.18L115.73 24.23L115.70 24.21Q115.74 23.60 115.93 22.49L115.97 22.53L115.91 22.47Q120.98 22.67 125.01 21.03L125.04 21.06L124.94 20.96Q125.34 19.53 126.30 16.72L126.28 16.70L124.16 17.63L124.21 17.67Q124.54 16.49 125.04 15.35L125.17 15.48L125.20 15.51Q121.37 16.97 117.26 17.05L117.19 16.97L117.11 16.89Q113.06 17.08 109.11 15.97L109.10 15.97L109.03 15.89Q109.88 20.48 109.88 24.89L109.81 24.82L109.79 24.81Q109.79 26.70 109.67 28.61L109.77 28.71L109.66 28.59Q110.00 28.86 110.57 29.16L110.54 29.13L110.55 29.14Q110.85 28.88 111.50 28.53L111.50 28.53L111.44 28.47Q111.43 29.26 111.21 30.79L111.21 30.79L111.24 30.82Q111.73 31.08 112.15 31.31L112.10 31.26L112.04 31.20Q114.88 29.51 116.75 29.51L116.64 29.40L116.78 29.55Q118.07 29.50 119.25 30.15L119.23 30.13L119.21 30.11Q119.62 31.21 119.66 32.16L119.56 32.06L119.68 32.18Q119.71 34.73 118.69 35.83L118.65 35.80L118.68 35.83Q117.33 37.06 115.08 37.29L115.05 37.25L115.02 37.22Q114.12 37.36 113.44 37.28L113.48 37.33L113.35 37.20Q112.49 37.06 111.73 36.72L111.74 36.73L111.86 36.66L111.58 36.61L111.62 36.65Q110.95 36.28 110.42 34.95L110.27 34.80L110.27 34.80Q109.09 36.37 107.42 38.50L107.31 38.38L107.26 38.34Q107.59 39.01 108.43 39.96L108.52 40.06L108.39 39.93Q109.57 41.87 112.39 42.36L112.38 42.36L112.36 42.33Q113.54 42.56 118.90 42.67Z"/></svg>"""
load_captcha_data("../data/captcha_data.npz")
print(solve_captcha(example_svg))  # 6535

example_svg_2 = """<svg xmlns="http://www.w3.org/2000/svg" width="150" height="50" viewBox="0,0,150,50"><path fill="#444" d="M24.07 40.41L24.12 40.46L24.06 40.39Q20.02 40.66 19.03 38.34L19.08 38.38L19.07 38.38Q19.79 37.39 21.35 35.60L21.30 35.54L21.26 35.50Q21.83 37.59 24.83 37.71L24.84 37.71L24.86 37.74Q28.26 37.82 29.90 36.49L29.91 36.50L29.83 36.42Q31.24 34.83 31.17 32.12L31.16 32.11L31.26 32.22Q30.92 26.97 26.12 27.20L26.26 27.33L26.16 27.24Q23.48 27.52 21.73 28.78L21.69 28.74L21.36 28.56L21.08 28.36L21.06 28.34Q21.40 25.18 21.29 22.44L21.37 22.52L21.42 22.57Q21.25 19.89 20.91 16.58L20.82 16.49L20.95 16.61Q24.60 17.56 28.40 17.45L28.28 17.32L28.42 17.46Q32.05 17.21 35.63 15.96L35.74 16.06L35.09 17.51L35.20 17.61Q34.87 18.35 34.68 19.19L34.62 19.13L34.61 19.13Q31.62 20.28 27.74 20.28L27.66 20.20L27.57 20.11Q26.11 20.10 24.63 19.95L24.70 20.02L24.70 20.03Q24.56 20.64 24.22 25.10L24.39 25.27L24.30 25.18Q25.22 24.81 27.28 24.66L27.14 24.52L27.17 24.55Q30.95 24.83 32.40 26.50L32.43 26.53L32.47 26.57Q33.72 27.98 33.99 31.82L34.11 31.95L34.01 31.84Q34.29 36.04 33.07 38.06L33.04 38.04L33.12 38.11Q30.97 39.88 27.66 40.11L27.70 40.16L27.64 40.10Q26.74 40.26 24.07 40.41ZM30.16 42.73L30.18 42.75L30.01 42.58Q33.56 42.78 35.47 41.68L35.46 41.67L35.36 41.57Q36.36 40.06 36.36 37.97L36.47 38.08L36.43 38.03Q36.50 35.02 35.55 30.91L35.44 30.80L35.51 30.87Q35.06 29.05 33.84 27.64L33.95 27.75L33.81 27.65L33.65 27.42L33.35 27.26L33.32 27.24Q33.03 26.52 32.38 25.84L32.32 25.78L32.39 25.89L32.39 25.89Q30.91 24.25 27.22 24.25L27.26 24.30L26.90 24.20L26.95 24.26Q26.99 23.65 27.18 22.55L27.26 22.62L27.22 22.58Q32.19 22.68 36.23 21.05L36.15 20.97L36.21 21.03Q36.57 19.56 37.52 16.74L37.57 16.79L35.38 17.65L35.41 17.67Q35.81 16.55 36.31 15.41L36.42 15.52L36.39 15.50Q32.42 16.82 28.31 16.90L28.31 16.90L28.32 16.91Q24.20 17.01 20.24 15.91L20.28 15.95L20.39 16.06Q20.96 20.36 20.96 24.77L20.91 24.73L21.00 24.81Q20.92 26.63 20.80 28.54L20.84 28.58L20.83 28.57Q21.09 28.74 21.66 29.05L21.74 29.13L21.77 29.16Q22.08 28.90 22.73 28.56L22.80 28.63L22.64 28.47Q22.73 29.36 22.50 30.89L22.47 30.85L22.48 30.87Q22.92 31.08 23.34 31.30L23.28 31.24L23.27 31.23Q26.03 29.47 27.90 29.47L27.95 29.51L28.01 29.58Q29.25 29.48 30.43 30.13L30.46 30.16L30.49 30.20Q30.86 31.25 30.90 32.20L30.78 32.08L30.89 32.19Q30.80 34.61 29.77 35.72L29.96 35.91L29.78 35.72Q28.42 36.96 26.18 37.19L26.34 37.34L26.34 37.34Q25.25 37.28 24.56 37.21L24.67 37.32L24.69 37.33Q23.76 37.13 23.00 36.79L23.07 36.86L23.07 36.67L22.87 36.69L22.83 36.65Q22.11 36.24 21.57 34.90L21.55 34.88L21.54 34.87Q20.21 36.28 18.54 38.41L18.44 38.32L18.50 38.38Q18.83 39.05 19.67 40.00L19.72 40.05L19.75 40.09Q20.72 41.82 23.54 42.32L23.48 42.25L23.63 42.41Q24.71 42.53 30.08 42.65Z"/><path d="M20 22 C87 5,65 28,146 10" stroke="#444" fill="none"/><path fill="#222" d="M52.36 32.95L52.42 33.01L52.40 32.99Q55.36 32.49 58.56 32.60L58.68 32.72L58.74 32.79Q58.65 30.18 58.65 27.78L58.70 27.83L58.69 27.82Q58.53 25.19 58.72 22.64L58.78 22.69L58.81 22.72Q57.53 24.38 52.32 32.91ZM62.24 40.28L62.20 40.24L62.25 40.29Q60.52 39.93 58.73 39.86L58.78 39.90L58.89 40.02Q58.53 37.48 58.41 35.01L58.42 35.01L58.56 35.15Q53.20 34.94 48.48 36.34L48.37 36.23L48.46 36.32Q48.56 35.82 48.75 34.83L48.69 34.76L48.79 34.86Q50.48 31.61 54.06 25.33L54.05 25.31L54.08 25.34Q57.06 20.55 60.48 16.67L60.34 16.53L60.52 16.70Q61.24 16.36 62.91 16.09L62.90 16.08L62.90 16.08Q61.01 22.53 61.01 29.57L61.04 29.60L61.14 29.70Q61.11 31.15 61.18 32.64L61.12 32.58L62.54 32.82L62.51 32.79Q63.11 32.82 63.72 32.93L63.59 32.79L63.68 32.89Q63.87 33.96 64.14 35.90L63.97 35.73L64.12 35.87Q62.79 35.50 61.31 35.31L61.31 35.31L61.41 35.41Q61.56 37.35 62.24 40.28ZM63.89 32.45L63.94 32.50L63.88 32.44Q63.79 32.47 63.60 32.47L63.53 32.40L63.23 32.48L63.18 32.43Q63.04 30.92 63.04 29.51L63.13 29.60L62.98 29.44Q63.01 23.08 65.07 17.07L65.18 17.18L65.15 17.15Q64.41 17.44 62.97 17.82L62.99 17.85L62.96 17.81Q63.22 17.08 63.68 15.68L63.55 15.55L63.50 15.50Q62.21 15.88 60.15 16.11L60.17 16.13L60.17 16.13Q56.40 20.62 51.18 29.99L51.08 29.88L53.12 26.17L53.14 26.19Q52.75 27.25 52.48 27.82L52.48 27.82L48.06 36.88L48.02 36.83Q48.66 36.68 49.81 36.30L49.78 36.27L49.65 36.52L49.71 36.58Q49.49 37.16 49.19 38.42L49.34 38.57L49.38 38.61Q53.43 37.22 58.27 37.41L58.24 37.38L58.24 37.38Q58.30 38.35 58.49 40.33L58.44 40.28L58.54 40.39Q59.51 40.29 60.58 40.41L60.64 40.47L60.55 40.38Q60.71 41.07 60.98 42.44L61.10 42.57L61.04 42.50Q62.82 42.61 65.82 43.52L65.98 43.68L65.91 43.61Q64.84 41.39 63.92 38.12L64.09 38.29L65.39 38.60L65.47 38.67Q66.25 38.99 66.93 39.34L66.92 39.33L66.87 39.28Q66.12 36.81 65.97 35.14L65.80 34.97L65.91 35.07Q65.39 34.98 64.25 34.75L64.16 34.66L64.13 34.63Q63.94 33.37 63.94 32.50ZM55.97 32.37L55.86 32.26L55.91 32.31Q56.81 31.15 58.37 28.60L58.34 28.58L58.34 28.57Q58.23 29.41 58.19 30.36L58.30 30.48L58.20 30.37Q58.16 31.33 58.20 32.28L58.22 32.30L58.26 32.34Q57.64 32.25 57.07 32.25L57.11 32.29L57.17 32.36Q56.54 32.33 55.93 32.33Z"/><path fill="#333" d="M86.44 23.35L86.49 23.39L86.45 23.36Q83.36 23.46 81.54 22.40L81.48 22.35L81.51 22.37Q83.95 20.93 88.83 16.71L88.89 16.77L88.85 16.73Q89.66 16.63 90.95 16.02L90.88 15.94L90.84 15.91Q89.49 21.83 89.38 28.19L89.50 28.31L89.43 28.24Q89.22 34.50 90.28 40.59L90.32 40.62L90.33 40.63Q88.72 39.98 86.59 39.86L86.56 39.83L86.52 39.79Q86.53 35.77 86.53 31.70L86.51 31.68L86.43 31.60Q86.47 27.53 86.51 23.42ZM86.21 25.74L86.16 40.27L86.12 40.23Q87.28 40.18 88.24 40.37L88.25 40.38L88.30 40.43Q88.45 41.19 88.64 42.56L88.48 42.40L88.59 42.51Q91.34 42.94 93.78 45.19L93.82 45.23L93.91 45.32Q91.29 38.05 91.25 30.59L91.31 30.65L91.32 30.66Q91.34 23.29 93.17 16.06L93.13 16.03L93.09 15.98Q92.55 16.40 90.95 17.50L90.91 17.46L90.97 17.52Q91.06 16.65 91.36 15.13L91.38 15.15L91.48 15.25Q90.20 16.07 88.76 16.45L88.76 16.45L88.69 16.38Q84.95 19.99 80.65 22.27L80.63 22.25L80.50 22.12Q82.10 23.42 84.46 23.76L84.37 23.67L84.38 23.69Q83.71 24.20 82.42 25.26L82.52 25.36L82.38 25.23Q83.88 25.62 86.09 25.62L86.07 25.60Z"/><path fill="#111" d="M112.92 36.98L112.80 36.85L112.94 36.99Q114.03 37.85 115.43 37.70L115.41 37.67L115.42 37.69Q118.37 37.90 119.02 34.55L119.00 34.53L119.03 34.55Q119.55 31.31 119.55 27.92L119.53 27.90L119.52 25.30L119.56 25.34Q119.67 24.19 119.32 22.94L119.24 22.85L119.20 22.81Q118.11 25.26 116.13 30.02L116.01 29.90L116.09 29.98Q114.15 34.77 112.93 36.98ZM117.83 20.37L117.86 20.41L117.90 20.44Q116.69 19.58 115.36 19.58L115.48 19.70L115.32 19.54Q113.86 19.41 112.76 20.33L112.89 20.46L112.91 20.48Q111.66 21.25 111.47 22.73L111.58 22.85L111.57 22.84Q111.26 24.23 111.22 25.72L111.05 25.55L111.11 25.61Q111.11 25.61 111.11 28.47L111.15 28.51L111.25 28.60Q111.23 30.94 111.69 34.56L111.57 34.44L111.58 34.46Q113.49 29.71 117.87 20.42ZM119.45 39.24L119.54 39.33L119.43 39.23Q117.60 40.05 115.28 40.05L115.37 40.15L113.65 40.07L113.77 40.19Q110.57 40.22 109.43 38.51L109.34 38.42L109.30 38.38Q108.47 36.18 108.39 33.25L108.45 33.30L108.46 33.32Q108.36 31.50 108.28 28.03L108.29 28.04L108.34 28.09Q108.26 26.83 108.11 23.79L108.16 23.84L108.22 23.90Q108.10 21.57 108.41 19.59L108.45 19.64L108.46 19.64Q108.89 16.65 113.23 16.42L113.30 16.49L113.28 16.47Q114.06 16.46 115.40 16.49L115.27 16.37L115.39 16.49Q121.00 16.58 122.06 20.04L122.13 20.11L122.06 20.03Q122.75 22.02 122.71 23.89L122.64 23.82L122.64 23.82Q122.51 28.75 122.43 29.96L122.44 29.97L122.59 30.12Q122.32 33.85 122.01 35.14L121.90 35.03L122.00 35.12Q121.28 38.18 119.38 39.17ZM124.44 39.05L124.36 38.97L124.30 38.91Q124.62 36.22 124.58 34.43L124.67 34.53L124.45 29.78L124.53 29.86Q124.40 26.79 123.87 21.27L123.90 21.30L123.85 21.26Q123.38 19.49 122.09 18.73L122.02 18.67L121.98 18.62Q120.43 16.09 115.25 15.93L115.25 15.93L115.33 16.01Q114.46 15.97 113.12 16.01L113.19 16.08L113.09 15.97Q108.64 16.13 108.14 19.25L108.10 19.21L108.03 19.14Q107.70 21.52 107.82 23.61L107.83 23.62L107.74 23.53Q108.09 27.92 108.05 31.27L108.09 31.31L108.06 31.28Q108.06 35.01 108.18 36.04L108.27 36.13L108.25 36.11Q108.66 39.22 110.18 40.02L110.05 39.89L110.13 39.97Q111.64 42.21 115.64 42.47L115.60 42.43L115.63 42.46Q119.18 42.66 119.83 42.62L119.83 42.63L119.89 42.69Q122.75 42.54 123.89 40.94L123.73 40.78L123.79 40.84Q124.42 40.29 124.49 39.11ZM115.77 37.27L115.71 37.21L115.81 37.31Q116.40 35.78 117.47 33.07L117.64 33.24L119.29 28.96L119.34 29.00Q119.28 30.62 118.90 33.97L118.76 33.83L118.84 33.91Q118.24 36.85 115.84 37.35ZM113.88 25.07L113.73 24.92L113.78 24.97Q114.23 23.17 114.91 22.60L114.87 22.56L115.02 22.71Q115.36 22.16 116.65 21.97L116.73 22.06L116.62 21.94Q114.93 25.62 113.07 30.27L113.05 30.25L113.09 30.29Q113.10 27.60 113.78 24.97Z"/></svg>"""
print(solve_captcha(example_svg_2))  # 5410
