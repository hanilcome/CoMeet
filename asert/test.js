{% verbatim %}  
// verbatim : '그대로','축어적인'라는 뜻이래요... 어렵다 영어

<script>
function enableEdit() {
  // readonly 속성 제거
  document.getElementById("username").readOnly = false;
  document.getElementById("email").readOnly = false;
  
  // 저장 버튼 보이게 하고, 편집 버튼 숨기기
  document.getElementsByTagName("button")[0].style.display = "none";
  document.getElementsByTagName("button")[1].style.display = "inline-block";
}
</script>
{% endverbatim %}
