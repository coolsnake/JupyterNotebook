# import bs4
# import requests
# import pprint
# from collections import defaultdict
# from bs4 import BeautifulSoup

# with open('algo_list(1).html', 'r') as f:

#     contents = f.read()
    
#     soup = BeautifulSoup(contents, 'lxml')

#     most_recent_key=""
#     result=defaultdict(list)
#     for tag in soup.find_all(['h3', 'li']):
#         # if tag.name=="li":
#         #     to_con= tag.text.split(':')[0]
#         if tag.name=="h3":
#             most_recent_key= tag.text.split('[')[0]
#             if tag.text not in result:
#                 tags= tag.text.split('[')[0]
#                 result[tags]=[]
#         elif tag.name!="h3":
#             to_con= tag.text.split(':')[0].splitlines()
#             for i in to_con:
#                 i=i.replace(" ", "+")
#                 result[most_recent_key].append(i)
# result2 = {}
# for i, k in result.items():
#     result2[i]=k    
# for i, k in result.items():
#     if len(k)==0:
#         result2.pop(i)
# print(result2)
result2= {'General combinatorial algorithms': ["Brent's+algorithm", "Floyd's+cycle-finding+algorithm", 'Gale–Shapley+algorithm', 'Pseudorandom+number+generators+(uniformly+distributed—see+also+List+of+pseudorandom+number+generators+for+other+PRNGs+with+varying+degrees+of+convergence+and+varying+statistical+quality)', 'ACORN+generator', 'Blum+Blum+Shub', 'Lagged+Fibonacci+generator', 'Linear+congruential+generator', 'Mersenne+Twister'], 'Graph algorithms': ['Coloring+algorithm', 'Hopcroft–Karp+algorithm', 'Hungarian+algorithm', 'Prüfer+coding', "Tarjan's+off-line+lowest+common+ancestors+algorithm", 'Topological+sort', 'Force-based+algorithms+(also+known+as+force-directed+algorithms+or+spring-based+algorithm)', 'Spectral+layout', 'Network+analysis', 'Link+analysis', 'Girvan–Newman+algorithm', 'Link+analysis', 'Girvan–Newman+algorithm', 'Girvan–Newman+algorithm', 'Web+link+analysis', 'Hyperlink-Induced+Topic+Search+(HITS)+(also+known+as+Hubs+and+authorities)', 'PageRank', 'TrustRank', 'Hyperlink-Induced+Topic+Search+(HITS)+(also+known+as+Hubs+and+authorities)', 'PageRank', 'TrustRank', 'Flow+networks', "Dinic's+algorithm", "Dinic's+algorithm", 'Edmonds–Karp+algorithm', 'Ford–Fulkerson+algorithm', "Karger's+algorithm", 'Push–relabel+algorithm', "Edmonds'+algorithm+(also+known+as+Chu–Liu/Edmonds'+algorithm)", 'Euclidean+minimum+spanning+tree', 'Euclidean+shortest+path+problem', 'Longest+path+problem', 'Minimum+spanning+tree', "Borůvka's+algorithm", "Kruskal's+algorithm", "Prim's+algorithm", 'Reverse-delete+algorithm', "Borůvka's+algorithm", "Kruskal's+algorithm", "Prim's+algorithm", 'Reverse-delete+algorithm', 'Nonblocking+minimal+spanning+switch+say,+for+a+telephone+exchange', 'Shortest+path+problem', 'Bellman–Ford+algorithm', 'Bellman–Ford+algorithm', "Dijkstra's+algorithm", 'Floyd–Warshall+algorithm', "Johnson's+algorithm", 'Transitive+closure+problem', 'Traveling+salesman+problem', 'Christofides+algorithm', 'Nearest+neighbour+algorithm', 'Christofides+algorithm', 'Nearest+neighbour+algorithm', "Warnsdorff's+rule", 'A*', 'B*', 'Backtracking', 'Beam+search', 'Beam+stack+search', 'Best-first+search', 'Bidirectional+search', 'Breadth-first+search', 'Brute-force+search', 'D*', 'Depth-first+search', "Dijkstra's+algorithm", 'General+Problem+Solver', 'Iterative+deepening+depth-first+search+(IDDFS)', 'Jump+point+search', 'Lexicographic+breadth-first+search+(also+known+as+Lex-BFS)', 'Uniform-cost+search', 'SSS*', 'F*', 'Cliques', 'Bron–Kerbosch+algorithm', 'Bron–Kerbosch+algorithm', 'MaxCliqueDyn+maximum+clique+algorithm', 'Strongly+connected+components', 'Path-based+strong+component+algorithm', "Kosaraju's+algorithm", "Tarjan's+strongly+connected+components+algorithm", 'Path-based+strong+component+algorithm', "Kosaraju's+algorithm", "Tarjan's+strongly+connected+components+algorithm", 'Subgraph+isomorphism+problem'], 'Sequence algorithms': ['Bitap+algorithm', 'Phonetic+algorithms', 'Daitch–Mokotoff+Soundex', 'Daitch–Mokotoff+Soundex', 'Double+Metaphone', 'Match+rating+approach', 'Metaphone', 'NYSIIS', 'Soundex', 'String+metrics', 'Damerau–Levenshtein+distance+compute+a+distance+measure+between+two+strings,+improves+on+Levenshtein+distance', "Dice's+coefficient+(also+known+as+the+Dice+coefficient)", 'Hamming+distance', 'Jaro–Winkler+distance', 'Levenshtein+edit+distance', 'Trigram+search', 'Quickselect', 'Introselect', 'Linear+search', 'Selection+algorithm', 'Ternary+search', 'Sorted+lists', 'Binary+search+algorithm', 'Binary+search+algorithm', 'Fibonacci+search+technique', 'Jump+search+(or+block+search)', 'Predictive+search', 'Uniform+binary+search', 'Simple+merge+algorithm', 'k-way+merge+algorithm', 'Union+(merge,+with+elements+on+the+output+not+repeated)', 'Fisher–Yates+shuffle+(also+known+as+the+Knuth+shuffle)', 'Schensted+algorithm', 'Steinhaus–Johnson–Trotter+algorithm+(also+known+as+the+Johnson–Trotter+algorithm)', "Heap's+permutation+generation+algorithm", 'Dynamic+time+warping', "Hirschberg's+algorithm", 'Needleman–Wunsch+algorithm', 'Smith–Waterman+algorithm', 'Exchange+sorts', 'Bubble+sort', 'Bubble+sort', 'Cocktail+shaker+sort+or+bidirectional+bubble+sort,+a+bubble+sort+traversing+the+list+alternately+from+front+to+back+and+back+to+front', 'Comb+sort', 'Gnome+sort', 'Odd–even+sort', 'Quicksort', 'Humorous+or+ineffective', 'Bogosort', 'Stooge+sort', 'Bogosort', 'Stooge+sort', 'Hybrid', 'Flashsort', 'Introsort', 'Flashsort', 'Introsort', 'Timsort', 'Insertion+sorts', 'Insertion+sort', 'Insertion+sort', 'Library+sort', 'Patience+sorting', 'Shell+sort', 'Tree+sort+(binary+tree+sort)', 'Cycle+sort', 'Merge+sorts', 'Merge+sort', 'Merge+sort', 'Slowsort', 'Strand+sort', 'Non-comparison+sorts', 'Bead+sort', 'Bucket+sort', 'Burstsort', 'Bead+sort', 'Bucket+sort', 'Burstsort', 'Counting+sort', 'Pigeonhole+sort', 'Postman+sort', 'Radix+sort', 'Selection+sorts', 'Heapsort', 'Heapsort', 'Selection+sort', 'Smoothsort', 'Other', 'Bitonic+sorter', 'Pancake+sorting', 'Spaghetti+sort', 'Topological+sort', 'Bitonic+sorter', 'Pancake+sorting', 'Spaghetti+sort', 'Topological+sort', 'Unknown+class', 'Samplesort', 'Samplesort', "Kadane's+algorithm", 'Longest+common+subsequence+problem', 'Longest+increasing+subsequence+problem', 'Shortest+common+supersequence+problem', 'Longest+common+substring+problem', 'Substring+search', 'Aho–Corasick+string+matching+algorithm', 'Aho–Corasick+string+matching+algorithm', 'Boyer–Moore+string-search+algorithm', 'Boyer–Moore–Horspool+algorithm', 'Knuth–Morris–Pratt+algorithm', 'Rabin–Karp+string+search+algorithm', 'Zhu–Takaoka+string+matching+algorithm', "Ukkonen's+algorithm", 'Matching+wildcards', "Rich+Salz'+wildmat", "Rich+Salz'+wildmat", 'Krauss+matching+wildcards+algorithm'], 'Abstract algebra': ['Chien+search', 'Schreier–Sims+algorithm', 'Todd–Coxeter+algorithm'], 'Computer algebra': ["Buchberger's+algorithm", 'Cantor–Zassenhaus+algorithm', 'Faugère+F4+algorithm', "Gosper's+algorithm", 'Knuth–Bendix+completion+algorithm', 'Multivariate+division+algorithm', "Pollard's+kangaroo+algorithm+(also+known+as+Pollard's+lambda+algorithm+)", 'Polynomial+long+division', 'Risch+algorithm'], 'Geometry': ['Closest+pair+problem', 'Collision+detection+algorithms', 'Cone+algorithm', 'Convex+hull+algorithms', 'Graham+scan', 'Quickhull', 'Gift+wrapping+algorithm+or+Jarvis+march', "Chan's+algorithm", 'Kirkpatrick–Seidel+algorithm', 'Euclidean+distance+transform', 'Geometric+hashing', 'Gilbert–Johnson–Keerthi+distance+algorithm', 'Jump-and-Walk+algorithm', 'Laplacian+smoothing', 'Line+segment+intersection', 'Bentley–Ottmann+algorithm', 'Shamos–Hoey+algorithm', 'Minimum+bounding+box+algorithms', 'Nearest+neighbor+search', 'Point+in+polygon+algorithms', 'Point+set+registration+algorithms', 'Rotating+calipers', 'Shoelace+algorithm', 'Triangulation', 'Delaunay+triangulation', "Ruppert's+algorithm+(also+known+as+Delaunay+refinement)", 'Delaunay+triangulation', "Ruppert's+algorithm+(also+known+as+Delaunay+refinement)", "Ruppert's+algorithm+(also+known+as+Delaunay+refinement)", "Chew's+second+algorithm", 'Marching+triangles', 'Polygon+triangulation+algorithms', 'Voronoi+diagrams,+geometric+dual+of+Delaunay+triangulation', 'Bowyer–Watson+algorithm', 'Bowyer–Watson+algorithm', "Fortune's+Algorithm", 'Quasitriangulation'], 'Number theoretic algorithms': ['Binary+GCD+algorithm', "Booth's+multiplication+algorithm", 'Chakravala+method', 'Discrete+logarithm', 'Baby-step+giant-step', 'Index+calculus+algorithm', "Pollard's+rho+algorithm+for+logarithms", 'Pohlig–Hellman+algorithm', 'Euclidean+algorithm', 'Extended+Euclidean+algorithm', 'Integer+factorization', 'Congruence+of+squares', "Dixon's+algorithm", "Fermat's+factorization+method", 'General+number+field+sieve', 'Lenstra+elliptic+curve+factorization', "Pollard's+p\xa0−\xa01+algorithm", "Pollard's+rho+algorithm", 'prime+factorization+algorithm', 'Quadratic+sieve', "Shor's+algorithm", 'Special+number+field+sieve', 'Trial+division', 'Multiplication+algorithms', 'Karatsuba+algorithm', 'Schönhage–Strassen+algorithm', 'Toom–Cook+multiplication', 'Modular+square+root', 'Tonelli–Shanks+algorithm', "Cipolla's+algorithm", "Berlekamp's+root+finding+algorithm", 'Odlyzko–Schönhage+algorithm', 'Lenstra–Lenstra–Lovász+algorithm+(also+known+as+LLL+algorithm)', 'Primality+tests', 'AKS+primality+test', 'Baillie-PSW+primality+test', 'Fermat+primality+test', 'Lucas+primality+test', 'Miller–Rabin+primality+test', 'Sieve+of+Atkin', 'Sieve+of+Eratosthenes', 'Sieve+of+Sundaram'], 'Numerical algorithms': ['Euler+method', 'Backward+Euler+method', 'Trapezoidal+rule+(differential+equations)', 'Linear+multistep+methods', 'Runge–Kutta+methods', 'Euler+integration', 'Euler+integration', 'Multigrid+methods+(MG+methods),+a+group+of+algorithms+for+solving+differential+equations+using+a+hierarchy+of+discretizations', 'Partial+differential+equation', 'Finite+difference+method', 'Crank–Nicolson+method+for+diffusion+equations', 'Lax-Wendroff+for+wave+equations', 'Verlet+integration+(French+pronunciation', 'Computation+of+π', "Borwein's+algorithm", 'Gauss–Legendre+algorithm', 'Chudnovsky+algorithm', 'Bailey–Borwein–Plouffe+formula', 'Division+algorithms', 'Long+division', 'Restoring+division', 'Non-restoring+division', 'SRT+division', 'Newton–Raphson+division', 'Goldschmidt+division', 'Hyperbolic+and+Trigonometric+Functions', 'BKM+algorithm', 'CORDIC', 'Exponentiation', 'Addition-chain+exponentiation', 'Exponentiating+by+squaring', 'Montgomery+reduction', 'Multiplication+algorithms', "Booth's+multiplication+algorithm", "Fürer's+algorithm", 'Karatsuba+algorithm', 'Schönhage–Strassen+algorithm', 'Toom–Cook+multiplication', 'Multiplicative+inverse+Algorithms', "Newton's+method", 'Rounding+functions', 'Spigot+algorithm', 'Square+and+Nth+root+of+a+number', 'Alpha+max+plus+beta+min+algorithm', 'Methods+of+computing+square+roots', 'nth+root+algorithm', 'Shifting+nth-root+algorithm', 'Summation', 'Binary+splitting', 'Kahan+summation+algorithm', 'Unrestricted+algorithm', 'Filtered+back-projection', 'Level+set+method+(LSM)', 'Birkhoff+interpolation', 'Cubic+interpolation', 'Hermite+interpolation', 'Lagrange+interpolation', 'Linear+interpolation', 'Monotone+cubic+interpolation', 'Multivariate+interpolation', 'Bicubic+interpolation,+a+generalization+of+cubic+interpolation+to+two+dimensions', 'Bilinear+interpolation', 'Bicubic+interpolation,+a+generalization+of+cubic+interpolation+to+two+dimensions', 'Bilinear+interpolation', 'Lanczos+resampling+("Lanzosh")', 'Nearest-neighbor+interpolation', 'Tricubic+interpolation,+a+generalization+of+cubic+interpolation+to+three+dimensions', 'Pareto+interpolation', 'Polynomial+interpolation', "Neville's+algorithm", "Neville's+algorithm", 'Spline+interpolation', 'De+Boor+algorithm', "De+Casteljau's+algorithm", 'Trigonometric+interpolation', 'Eigenvalue+algorithms', 'Arnoldi+iteration', 'Inverse+iteration', 'Jacobi+method', 'Lanczos+iteration', 'Power+iteration', 'QR+algorithm', 'Rayleigh+quotient+iteration', 'Arnoldi+iteration', 'Inverse+iteration', 'Jacobi+method', 'Lanczos+iteration', 'Power+iteration', 'QR+algorithm', 'Rayleigh+quotient+iteration', 'Gram–Schmidt+process', 'Matrix+multiplication+algorithms', "Cannon's+algorithm", "Cannon's+algorithm", 'Coppersmith–Winograd+algorithm', "Freivalds'+algorithm", 'Strassen+algorithm', 'Solving+systems+of+linear+equations', 'Biconjugate+gradient+method', 'Biconjugate+gradient+method', 'Conjugate+gradient', 'Gaussian+elimination', 'Gauss–Jordan+elimination', 'Gauss–Seidel+method', 'Levinson+recursion', "Stone's+method", 'Successive+over-relaxation+(SOR)', 'Tridiagonal+matrix+algorithm+(Thomas+algorithm)', 'Sparse+matrix+algorithms', 'Cuthill–McKee+algorithm', 'Cuthill–McKee+algorithm', 'Minimum+degree+algorithm', 'Symbolic+Cholesky+decomposition', 'Gibbs+sampling', 'Hybrid+Monte+Carlo', 'Metropolis–Hastings+algorithm', 'Wang+and+Landau+algorithm', 'MISER+algorithm', 'Bisection+method', 'False+position+method', "Newton's+method", "Halley's+method", 'Secant+method', 'False+position+method+and+Illinois+method', "Ridder's+method", "Muller's+method"], 'Optimization algorithms': ['Alpha–beta+pruning', 'Branch+and+bound', 'Bruss+algorithm', 'Chain+matrix+multiplication', 'Combinatorial+optimization', 'Greedy+randomized+adaptive+search+procedure+(GRASP)', 'Hungarian+method', 'Constraint+satisfaction', 'General+algorithms+for+the+constraint+satisfaction', 'AC-3+algorithm', 'Difference+map+algorithm', 'Min+conflicts+algorithm', 'Chaff+algorithm', 'General+algorithms+for+the+constraint+satisfaction', 'AC-3+algorithm', 'Difference+map+algorithm', 'Min+conflicts+algorithm', 'AC-3+algorithm', 'Difference+map+algorithm', 'Min+conflicts+algorithm', 'Chaff+algorithm', 'Davis–Putnam+algorithm', 'Davis–Putnam–Logemann–Loveland+algorithm+(DPLL)', 'Exact+cover+problem', 'Algorithm+X', 'Algorithm+X', 'Dancing+Links', 'Cross-entropy+method', 'Differential+evolution', 'Dynamic+Programming', 'Ellipsoid+method', 'Evolutionary+computation', 'Evolution+strategy', 'Gene+expression+programming', 'Genetic+algorithms', 'Fitness+proportionate+selection+-+also+known+as+roulette-wheel+selection', 'Stochastic+universal+sampling', 'Truncation+selection', 'Tournament+selection', 'Fitness+proportionate+selection+-+also+known+as+roulette-wheel+selection', 'Stochastic+universal+sampling', 'Truncation+selection', 'Tournament+selection', 'Memetic+algorithm', 'Swarm+intelligence', 'Ant+colony+optimization', 'Bees+algorithm', 'Ant+colony+optimization', 'Bees+algorithm', 'Particle+swarm', 'golden+section+search', 'Gradient+descent', 'Harmony+search+(HS)', 'Interior+point+method', 'Linear+programming', "Benson's+algorithm", "Benson's+algorithm", 'Dantzig–Wolfe+decomposition', 'Delayed+column+generation', 'Integer+linear+programming', 'Branch+and+cut', 'Cutting-plane+method', "Karmarkar's+algorithm", 'Simplex+algorithm', 'Line+search', 'Local+search', 'Random-restart+hill+climbing', 'Tabu+search', 'Minimax+used+in+game+programming', 'Nearest+neighbor+search+(NNS)', 'Best+Bin+First', "Newton's+method+in+optimization", 'Nonlinear+optimization', 'BFGS+method', 'BFGS+method', 'Gauss–Newton+algorithm', 'Levenberg–Marquardt+algorithm', 'Nelder–Mead+method+(downhill+simplex+method)', 'Odds+algorithm+(Bruss+algorithm)\xa0', 'Simulated+annealing', 'Stochastic+tunneling', 'Subset+sum+algorithm'], 'Astronomy': ['Doomsday+algorithm', "Zeller's+congruence+is+an+algorithm+to+calculate+the+day+of+the+week+for+any+Julian+or+Gregorian+calendar+date", 'various+Easter+algorithms+are+used+to+calculate+the+day+of+Easter'], 'Bioinformatics': ['Basic+Local+Alignment+Search+Tool+also+known+as+BLAST', 'Kabsch+algorithm', 'Velvet', 'Sorting+by+signed+reversals', 'Maximum+parsimony+(phylogenetics)', 'UPGMA'], 'Geoscience': ["Vincenty's+formulae", 'Geohash'], 'Linguistics': ['Lesk+algorithm', 'Stemming+algorithm', "Sukhotin's+algorithm"], 'Medicine': ['ESC+algorithm+for+the+diagnosis+of+heart+failure', 'Manning+Criteria+for+irritable+bowel+syndrome', 'Pulmonary+embolism+diagnostic+algorithms', 'Texas+Medication+Algorithm+Project'], 'Physics': ['Constraint+algorithm', 'Demon+algorithm', "Featherstone's+algorithm", 'Ground+state+approximation', 'Variational+method', 'Ritz+method', 'Variational+method', 'Ritz+method', 'Ritz+method', 'n-body+problems', 'Barnes–Hut+simulation', 'Barnes–Hut+simulation', 'Fast+multipole+method+(FMM)', 'Rainflow-counting+algorithm', 'Sweep+and+prune', 'VEGAS+algorithm'], 'Statistics': ['Algorithms+for+calculating+variance', 'Approximate+counting+algorithm', 'Bayesian+statistics', 'Nested+sampling+algorithm', 'Nested+sampling+algorithm', 'Clustering+Algorithms', 'Average-linkage+clustering', 'Average-linkage+clustering', 'Canopy+clustering+algorithm', 'Complete-linkage+clustering', 'DBSCAN', 'Expectation-maximization+algorithm', 'Fuzzy+clustering', 'Fuzzy+c-means', 'FLAME+clustering+(Fuzzy+clustering+by+Local+Approximation+of+MEmberships)', 'KHOPCA+clustering+algorithm', 'k-means+clustering', 'k-means++', 'k-medoids', 'Linde–Buzo–Gray+algorithm', "Lloyd's+algorithm+(Voronoi+iteration+or+relaxation)", 'OPTICS', 'Single-linkage+clustering', 'SUBCLU', "Ward's+method\xa0", 'WACA+clustering+algorithm', 'Estimation+Theory', 'Expectation-maximization+algorithm+A+class+of+related+algorithms+for+finding+maximum+likelihood+estimates+of+parameters+in+probabilistic+models', 'Ordered+subset+expectation+maximization+(OSEM)', 'Expectation-maximization+algorithm+A+class+of+related+algorithms+for+finding+maximum+likelihood+estimates+of+parameters+in+probabilistic+models', 'Ordered+subset+expectation+maximization+(OSEM)', 'Ordered+subset+expectation+maximization+(OSEM)', 'Odds+algorithm+(Bruss+algorithm)+Optimal+online+search+for+distinguished+value+in+sequential+random+input', 'Kalman+filter', 'False+nearest+neighbor+algorithm+(FNN)+estimates+fractal+dimension', 'Hidden+Markov+model', 'Baum–Welch+algorithm', 'Baum–Welch+algorithm', 'Forward-backward+algorithm+a+dynamic+programming+algorithm+for+computing+the+probability+of+a+particular+observation+sequence', 'Viterbi+algorithm', 'Partial+least+squares+regression', 'Queuing+theory', "Buzen's+algorithm", "Buzen's+algorithm", 'RANSAC+(an+abbreviation+for+"RANdom+SAmple+Consensus")', 'Scoring+algorithm', 'Yamartino+method', 'Ziggurat+algorithm'], 'Computer architecture': ['Tomasulo+algorithm'], 'Computer graphics': ['Clipping', 'Line+clipping', 'Cohen–Sutherland', 'Cyrus–Beck', 'Fast-clipping', 'Liang–Barsky', 'Nicholl–Lee–Nicholl', 'Polygon+clipping', 'Sutherland–Hodgman', 'Vatti', 'Weiler–Atherton', 'Line+clipping', 'Cohen–Sutherland', 'Cyrus–Beck', 'Fast-clipping', 'Liang–Barsky', 'Nicholl–Lee–Nicholl', 'Cohen–Sutherland', 'Cyrus–Beck', 'Fast-clipping', 'Liang–Barsky', 'Nicholl–Lee–Nicholl', 'Polygon+clipping', 'Sutherland–Hodgman', 'Vatti', 'Weiler–Atherton', 'Sutherland–Hodgman', 'Vatti', 'Weiler–Atherton', 'Contour+lines+and+Isosurfaces', 'Marching+cubes', 'Marching+cubes', 'Marching+squares', 'Marching+tetrahedrons', "Discrete+Green's+Theorem", 'Flood+fill', 'Global+illumination+algorithms', 'Ambient+occlusion', 'Beam+tracing', 'Cone+tracing', 'Image-based+lighting', 'Metropolis+light+transport', 'Path+tracing', 'Photon+mapping', 'Radiosity', 'Ray+tracing', 'Hidden+surface+removal+or+Visual+surface+determination', "Newell's+algorithm", "Newell's+algorithm", "Painter's+algorithm", 'Scanline+rendering', 'Warnock+algorithm', 'Line+Drawing', "Bresenham's+line+algorithm", 'DDA+line+algorithm', "Xiaolin+Wu's+line+algorithm", 'Midpoint+circle+algorithm', 'Ramer–Douglas–Peucker+algorithm', 'Shading', 'Gouraud+shading', 'Gouraud+shading', 'Phong+shading', 'Slerp+(spherical+linear+interpolation)', 'Summed+area+table+(also+known+as+an+integral+image)'], 'Cryptography': ['Asymmetric+(public+key)+encryption', 'ElGamal', 'Elliptic+curve+cryptography', 'MAE1', 'NTRUEncrypt', 'RSA', 'Digital+signatures+(asymmetric+authentication)', 'DSA,+and+its+variants', 'ECDSA+and+Deterministic+ECDSA', 'EdDSA+(Ed25519)', 'RSA', 'Cryptographic+hash+functions+(see+also+the+section+on+message+authentication+codes)', 'BLAKE', 'MD5+–+Note+that+there+is+now+a+method+of+generating+collisions+for+MD5', 'RIPEMD-160', 'SHA-1+–+Note+that+there+is+now+a+method+of+generating+collisions+for+SHA-1', 'SHA-2+(SHA-224,+SHA-256,+SHA-384,+SHA-512)', 'SHA-3+(SHA3-224,+SHA3-256,+SHA3-384,+SHA3-512,+SHAKE128,+SHAKE256)', 'Tiger+(TTH),+usually+used+in+Tiger+tree+hashes', 'WHIRLPOOL', 'Cryptographically+secure+pseudo-random+number+generators', 'Blum+Blum+Shub+-+based+on+the+hardness+of+factorization', 'Fortuna,+intended+as+an+improvement+on+Yarrow+algorithm', 'Linear-feedback+shift+register+(note', 'Blum+Blum+Shub+-+based+on+the+hardness+of+factorization', 'Fortuna,+intended+as+an+improvement+on+Yarrow+algorithm', 'Linear-feedback+shift+register+(note', 'Yarrow+algorithm', 'Key+exchange', 'Diffie–Hellman+key+exchange', 'Elliptic-curve+Diffie-Hellman+(ECDH)', 'Diffie–Hellman+key+exchange', 'Elliptic-curve+Diffie-Hellman+(ECDH)', 'Key+derivation+functions,+often+used+for+password+hashing+and+key+stretching', 'bcrypt', 'PBKDF2', 'scrypt', 'Argon2', 'bcrypt', 'PBKDF2', 'scrypt', 'Argon2', 'Message+authentication+codes+(symmetric+authentication+algorithms,+which+take+a+key+as+a+parameter)', 'HMAC', 'Poly1305', 'SipHash', 'Secret+sharing,+Secret+Splitting,+Key+Splitting,+M+of+N+algorithms', "Blakey's+Scheme", "Shamir's+Scheme", "Blakey's+Scheme", "Shamir's+Scheme", 'Symmetric+(secret+key)+encryption', 'Advanced+Encryption+Standard+(AES),+winner+of+NIST+competition,+also+known+as+Rijndael', 'Blowfish', 'Twofish', 'Threefish', 'Data+Encryption+Standard+(DES),+sometimes+DE+Algorithm,+winner+of+NBS+selection+competition,+replaced+by+AES+for+most+purposes', 'IDEA', 'RC4+(cipher)', 'Tiny+Encryption+Algorithm+(TEA)', 'Salsa20,+and+its+updated+variant+ChaCha20', 'Post-quantum+cryptography', 'Proof-of-work+algorithms'], 'Digital logic': ['Boolean+minimization', 'Quine–McCluskey+algorithm', 'Quine–McCluskey+algorithm', "Petrick's+method", 'Espresso+heuristic+logic+minimizer'], 'Machine learning and statistical classification': ['ALOPEX', 'Association+rule+learning', 'Apriori+algorithm', 'Eclat+algorithm', 'FP-growth+algorithm', 'One-attribute+rule', 'Zero-attribute+rule', 'Boosting+(meta-algorithm)', 'AdaBoost', 'BrownBoost', 'LogitBoost', 'LPBoost', 'Bootstrap+aggregating+(bagging)', 'Computer+Vision', 'Grabcut+based+on+Graph+cuts', 'Grabcut+based+on+Graph+cuts', 'Decision+Trees', 'C4.5+algorithm', 'C4.5+algorithm', 'ID3+algorithm+(Iterative+Dichotomiser+3)', 'Clustering', 'k-nearest+neighbors+(k-NN)', 'Linde–Buzo–Gray+algorithm', 'Locality-sensitive+hashing+(LSH)', 'Neural+Network', 'Backpropagation', 'Backpropagation', 'Hopfield+net', 'Perceptron', 'Pulse-coupled+neural+networks+(PCNN)', 'Radial+basis+function+network', 'Self-organizing+map', 'Random+forest', 'Reinforcement+Learning', 'Q-learning', 'State-Action-Reward-State-Action+(SARSA)', 'Temporal+difference+learning', 'Relevance+Vector+Machine+(RVM)', 'Supervised+Learning', 'Support+Vector+Machines+(SVM)', 'Structured+SVM', 'Winnow+algorithm'], 'Programming language theory': ['C3+linearization', "Chaitin's+algorithm", 'Hindley–Milner+type+inference+algorithm', 'Rete+algorithm', 'Sethi-Ullman+algorithm', 'CYK+algorithm', 'Earley+parser', 'GLR+parser', 'Inside-outside+algorithm', 'LL+parser', 'LR+parser', 'Canonical+LR+parser', 'LALR+(Look-ahead+LR)+parser', 'Operator-precedence+parser', 'SLR+(Simple+LR)+parser', 'Simple+precedence+parser', 'Packrat+parser', 'Recursive+descent+parser', 'Shunting+yard+algorithm', 'Pratt+parser', 'Lexical+analysis'], 'Quantum algorithms': ['Deutsch–Jozsa+algorithm', "Grover's+algorithm", "Shor's+algorithm", "Simon's+algorithm"], 'Theory of computation and automata': ["Hopcroft's+algorithm,+Moore's+algorithm,+and+Brzozowski's+algorithm", 'Powerset+construction', 'Tarski–Kuratowski+algorithm'], 'Coding theory': ['BCH+Codes', 'Berlekamp–Massey+algorithm', 'Peterson–Gorenstein–Zierler+algorithm', 'Reed–Solomon+error+correction', 'Berlekamp–Massey+algorithm', 'Peterson–Gorenstein–Zierler+algorithm', 'Reed–Solomon+error+correction', 'BCJR+algorithm', 'Forward+error+correction', 'Gray+code', 'Hamming+codes', 'Hamming(7,4)', 'Hamming(7,4)', 'Hamming+distance', 'Hamming+weight+(population+count)', 'Redundancy+checks', 'Adler-32', 'Cyclic+redundancy+check', 'Damm+algorithm', "Fletcher's+checksum", 'Longitudinal+redundancy+check+(LRC)', 'Luhn+algorithm', 'Adler-32', 'Cyclic+redundancy+check', 'Damm+algorithm', "Fletcher's+checksum", 'Longitudinal+redundancy+check+(LRC)', 'Luhn+algorithm', 'Luhn+mod+N+algorithm', 'Parity', 'Verhoeff+algorithm', 'Burrows–Wheeler+transform', 'Context+tree+weighting', 'Delta+encoding', 'Dynamic+Markov+compression', 'Dictionary+coders', 'Byte+pair+encoding+(BPE)', 'DEFLATE', 'Lempel–Ziv', 'LZ77+and+LZ78', 'Lempel–Ziv+Jeff+Bonwick+(LZJB)', 'Lempel–Ziv–Markov+chain+algorithm+(LZMA)', 'Lempel–Ziv–Oberhumer+(LZO)', 'Byte+pair+encoding+(BPE)', 'DEFLATE', 'Lempel–Ziv', 'LZ77+and+LZ78', 'Lempel–Ziv+Jeff+Bonwick+(LZJB)', 'Lempel–Ziv–Markov+chain+algorithm+(LZMA)', 'Lempel–Ziv–Oberhumer+(LZO)', 'LZ77+and+LZ78', 'Lempel–Ziv+Jeff+Bonwick+(LZJB)', 'Lempel–Ziv–Markov+chain+algorithm+(LZMA)', 'Lempel–Ziv–Oberhumer+(LZO)', 'Lempel–Ziv–Stac+(LZS)', 'Lempel–Ziv–Storer–Szymanski+(LZSS)', 'Lempel–Ziv–Welch+(LZW)', 'LZWL', 'LZX', 'Lempel–Ziv+Ross+Williams+(LZRW)', 'Entropy+encoding', 'Arithmetic+coding', 'Range+encoding', 'Huffman+coding', 'Adaptive+Huffman+coding', 'Package-merge+algorithm', 'Shannon–Fano+coding', 'Shannon–Fano–Elias+coding', 'Entropy+coding+with+known+entropy+characteristics', 'Golomb+coding', 'Golomb+coding', 'Rice+coding', 'Truncated+binary+encoding', 'Unary+coding', 'Universal+codes', 'Elias+delta,+gamma,+and+omega+coding', 'Exponential-Golomb+coding', 'Fibonacci+coding', 'Levenshtein+coding', 'Fast+Efficient+&+Lossless+Image+Compression+System+(FELICS)', 'Incremental+encoding', 'Prediction+by+partial+matching+(PPM)', 'Run-length+encoding', 'SEQUITUR+algorithm', '3Dc', 'Audio+and+Speech+compression', 'A-law+algorithm', 'A-law+algorithm', 'Code-excited+linear+prediction+(CELP)', 'Linear+predictive+coding+(LPC)', 'Mu-law+algorithm', 'Warped+Linear+Predictive+Coding+(WLPC)', 'Image+compression', 'Block+Truncation+Coding+(BTC)', 'Block+Truncation+Coding+(BTC)', 'Embedded+Zerotree+Wavelet+(EZW)', 'Fast+Cosine+Transform+algorithms+(FCT+algorithms)', 'Fractal+compression', 'Set+Partitioning+in+Hierarchical+Trees+(SPIHT)', 'Wavelet+compression', 'Transform+coding', 'Video+compression', 'Vector+quantization'], 'Digital signal processing': ['Adaptive-additive+algorithm+(AA+algorithm)', 'Discrete+Fourier+transform', "Bluestein's+FFT+algorithm", "Bruun's+FFT+algorithm", 'Cooley–Tukey+FFT+algorithm', 'Fast+Fourier+transform', 'Prime-factor+FFT+algorithm', "Rader's+FFT+algorithm", 'Fast+folding+algorithm', 'Gerchberg–Saxton+algorithm', 'Goertzel+algorithm', 'Karplus-Strong+string+synthesis', 'Contrast+Enhancement', 'Histogram+equalization', 'Histogram+equalization', 'Adaptive+histogram+equalization', 'Connected-component+labeling', 'Dithering+and+half-toning', 'Error+diffusion', 'Floyd–Steinberg+dithering', 'Ordered+dithering', 'Riemersma+dithering', 'Error+diffusion', 'Floyd–Steinberg+dithering', 'Ordered+dithering', 'Riemersma+dithering', 'Elser+difference-map+algorithm', 'Feature+detection', 'Canny+edge+detector', 'Canny+edge+detector', 'Generalised+Hough+transform', 'Hough+transform', 'Marr–Hildreth+algorithm', 'SIFT+(Scale-invariant+feature+transform)', 'SURF+(Speeded+Up+Robust+Features)', 'Richardson–Lucy+deconvolution', 'Blind+deconvolution', 'Median+filtering', 'Seam+carving', 'Segmentation', 'GrowCut+algorithm', 'Random+walker+algorithm', 'Region+growing', 'Watershed+transformation', 'Cache+algorithms', 'CHS+conversion', 'Double+dabble', 'Hash+Function', 'Fowler–Noll–Vo+hash+function', 'Pearson+hashing', 'Zobrist+hashing', 'Unicode+Collation+Algorithm', 'Xor+swap+algorithm', 'Algorithms+for+Recovery+and+Isolation+Exploiting+Semantics+(ARIES)', 'Join+algorithms', 'Block+nested+loop', 'Hash+join', 'Nested+loop+join', 'Sort-Merge+Join', 'Block+nested+loop', 'Hash+join', 'Nested+loop+join', 'Sort-Merge+Join', 'Bully+algorithm', 'Byzantine+fault+tolerance', 'Clock+synchronization', 'Berkeley+algorithm', "Cristian's+algorithm", 'Intersection+algorithm', "Marzullo's+algorithm", 'Berkeley+algorithm', "Cristian's+algorithm", 'Intersection+algorithm', "Marzullo's+algorithm", 'Detection+of+Process+Termination', 'Dijkstra-Scholten+algorithm', "Huang's+algorithm", 'Dijkstra-Scholten+algorithm', "Huang's+algorithm", 'Lamport+ordering', 'Mutual+exclusion', "Lamport's+Distributed+Mutual+Exclusion+Algorithm", "Naimi-Trehel's+log(n)+Algorithm", "Maekawa's+Algorithm", "Raymond's+Algorithm", 'Ricart-Agrawala+Algorithm', "Lamport's+Distributed+Mutual+Exclusion+Algorithm", "Naimi-Trehel's+log(n)+Algorithm", "Maekawa's+Algorithm", "Raymond's+Algorithm", 'Ricart-Agrawala+Algorithm', 'Paxos+algorithm', 'Raft+(computer+science)', 'Snapshot+algorithm', 'Chandy-Lamport+algorithm', 'Vector+clocks'], 'Memory allocation and deallocation algorithms': ['Buddy+memory+allocation', 'Garbage+collectors', "Cheney's+algorithm", "Cheney's+algorithm", 'Generational+garbage+collector', 'Mark-compact+algorithm', 'Mark+and+sweep', 'Semi-space+collector', 'Reference+counting', "Karn's+algorithm", 'Luleå+algorithm', 'Network+congestion', 'Exponential+backoff', "Nagle's+algorithm", 'Exponential+backoff', "Nagle's+algorithm", 'Truncated+binary+exponential+backoff', "Banker's+algorithm", 'Page+replacement+algorithms', 'Adaptive+replacement+cache', 'Clock+with+Adaptive+Replacement+(CAR)'], 'Process synchronization': ["Dekker's+algorithm", "Lamport's+Bakery+algorithm", "Peterson's+algorithm"], 'Scheduling': ['Earliest+deadline+first+scheduling', 'Fair-share+scheduling', 'Least+slack+time+scheduling', 'List+scheduling', 'Multi+level+feedback+queue', 'Rate-monotonic+scheduling', 'Round-robin+scheduling', 'Shortest+job+next', 'Shortest+remaining+time', 'Top-nodes+algorithm'], 'Input and output scheduling': ['Elevator+algorithm', 'Shortest+seek+first']}

for i,k in result2.items():
    for h in k:
        h=h.replace('3','+')
        # if "B*" in h:
        #     print(h)

#####################
# put results in to dictionary
import os 
import shutil  
newpath ='./'
source = ''
destination = ''
# for i in result2.keys():
#     newpath1=newpath+i
#     if not os.path.exists(newpath1):
#         os.makedirs(newpath1)    
# import os
for i,v in result2.items():
    for h in v:
        # try:
            for x in os.listdir('./'):
                if x.startswith(h) or (h in x):
                    source = newpath+x+"/"
                    destination = newpath+i+"/"
                    dest = shutil.move(source, destination) 
                    print (source + "->"+ destination)
                # else:
                #     print (x)
        # except:
        #     pass
        
    