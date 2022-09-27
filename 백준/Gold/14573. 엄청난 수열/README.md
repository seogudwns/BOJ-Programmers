# [Gold I] 엄청난 수열 - 14573 

[문제 링크](https://www.acmicpc.net/problem/14573) 

### 성능 요약

메모리: 208320 KB, 시간: 484 ms

### 분류

다이나믹 프로그래밍(dp), 수학(math), 누적 합(prefix_sum)

### 문제 설명

<p>얼마 전 dp를 공부하던 택희는 엄청난 사실을 알아냈다.</p>

<p>피보나치 수는 엄청나게 빠르게 증가한다는 것이다.</p>

<p>택희는 피보나치 수열에 엄청나게 매료되어 100만 번째 피보나치 수까지 종이에 적었다. 하지만 적는 도중 택희는 느꼈다. 피보나치 수 정도로는 엄청난 택희를 만족시켜줄 수가 없었다.</p>

<p>택희는 더 엄청나게 빨리 증가하는 수열이 없을까 생각하다가, 아래와 같은 엄청난 수열을 생각해냈다.</p>

<p>$$ a_1 = k $$</p>

<p>$$ N_n =\left\{ 1, 2, 3, 4, …, n \right\} 일 때, a_{n+1} = \sum_{S \subset N_n} \sum_{i \in S} a_i $$</p>

<p>즉, a<sub>n</sub>은 a<sub>1</sub>부터 a<sub>n-1</sub>까지의 수 중 하나 이상을 뽑아 만들 수 있는 모든 부분집합의 합으로 정의하였다.</p>

<p>예를 들어 a<sub>1</sub> = 1인 수열의 첫 몇 개 항을 살펴보면,</p>

<ul>
	<li>a<sub>2</sub> = a<sub>1</sub> = 1</li>
	<li>a<sub>3</sub> = (a<sub>1</sub>) + (a<sub>2</sub>) + (a<sub>1</sub> + a<sub>2</sub>) = 4</li>
	<li>a<sub>4</sub> = (a<sub>1</sub>) + (a<sub>2</sub>) + (a<sub>3</sub>) + (a<sub>1</sub> + a<sub>2</sub>) + (a<sub>1</sub> + a<sub>3</sub>) + (a<sub>2</sub> + a<sub>3</sub>) + (a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub>) = 24</li>
</ul>

<p>와 같다.</p>

<p>택희는 이 엄청난 수열이 피보나치 수열보다 더 빨리 증가한다는 사실을 증명했고, 이제 이 수를 종이에 적기 시작했다.</p>

<p>100만 번째 수를 적었을 때쯤, 택희는 궁금한 것이 여러 가지 생겼다.</p>

<p>예를 들어, a<sub>i</sub>와 a<sub>j</sub>의 최대공약수는 얼마인지, a<sub>k</sub>의 값은 무엇인지, 수열에서 연속된 일부를 뽑아 더하면 얼마인지, 만일 수열의 첫 항 a<sub>1</sub>이 바뀌면 이 값들은 어떻게 바뀌는지 등, 자신이 만든 엄청난 수열에 대해 점점 궁금한 것이 많아진 택희는 이를 빠르게 계산해 줄 프로그램이 필요하다고 판단했다.</p>

<p>택희를 위해 택희의 궁금증을 해결해 줄 프로그램을 작성해 보자.</p>

### 입력 

 <p>첫 줄에 택희의 질문의 개수 Q가 주어진다. (1 ≤ Q ≤ 200000)</p>

<p>이어 Q줄에 걸쳐, 다음의 네 가지 타입 중 하나의 쿼리가 주어진다.</p>

<ul>
	<li>1 a<sub>1</sub> i j (1 ≤ a<sub>1</sub> ≤ 10<sup>5</sup>, 1 ≤ i, j ≤ 10<sup>6</sup>): 첫 항이 a<sub>1</sub>인 엄청난 수열에서, a<sub>i</sub>와 a<sub>j</sub>의 최대공약수는?</li>
	<li>2 a<sub>1</sub> i j (1 ≤ a<sub>1</sub> ≤ 10<sup>5</sup>, 1 ≤ i, j ≤ 10<sup>6</sup>): 첫 항이 <!--[if gte msEquation 12]><m:oMath><m:sSub><m:sSubPr><span
   style='font-size:12.0pt;mso-ansi-font-size:12.0pt;mso-bidi-font-size:12.0pt;
   font-family:"Cambria Math";mso-ascii-font-family:"Cambria Math";mso-fareast-font-family:
   "맑은 고딕";mso-fareast-theme-font:minor-latin;mso-hansi-font-family:"Cambria Math"'><m:ctrlPr></m:ctrlPr></span></m:sSubPr><m:e><i
   style='mso-bidi-font-style:normal'><span style='font-size:12.0pt;line-height:
   160%;font-family:"Cambria Math";mso-fareast-font-family:"맑은 고딕";mso-fareast-theme-font:
   minor-latin'><m:r>a</m:r></span></i></m:e><m:sub><i style='mso-bidi-font-style:
   normal'><span style='font-size:12.0pt;line-height:160%;font-family:"Cambria Math";
   mso-fareast-font-family:"맑은 고딕";mso-fareast-theme-font:minor-latin'><m:r>1</m:r></span></i></m:sub></m:sSub></m:oMath><![endif]-->a<sub>1</sub>인 엄청난 수열에서, a<sub>i</sub>와 a<sub>j</sub>의 최소공배수는?
	<ul>
		<li>단, 이 값은 너무 클 수 있으므로, 이 값을 L이라 할 때, $ \frac{L}{2^P} $이 정수가 되게 하는 가장 큰 정수 P만 구해보자.</li>
	</ul>
	</li>
	<li>3 a<sub>1</sub> i j (1 ≤ a<sub>1</sub> ≤ 10<sup>5</sup>, 1 ≤ i, j ≤ 10<sup>6</sup>): 첫 항이 a<sub>1</sub>인 엄청난 수열에서, $ \sum_{k=i}^j a_k $는?</li>
	<li>4 a<sub>1</sub> k (1 ≤ a<sub>1</sub> ≤ 10<sup>5</sup>, 1 ≤ k ≤ 10<sup>6</sup>): 첫 항이 a<sub>1</sub>인 엄청난 수열에서, a<sub>k</sub>는?</li>
</ul>

<p>3번 쿼리의 경우, 항상 i ≤ j를 만족하도록 입력이 주어진다.</p>

### 출력 

 <p>Q줄에 걸쳐, 각 쿼리에 대한 답을 1,000,000,007로 나눈 나머지를 출력한다.</p>

