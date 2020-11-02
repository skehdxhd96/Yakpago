//입력페이지 Dynamic Select box 구현을 위한 javascript 함수
function insertSubcategories() {
    var category_select = document.getElementById('input_category');
    var subcategory_select = document.getElementById('input_subcategory');

    var category = category_select.value;
    
    fetch ('/subcategory/' + category).then(function(response) {
        response.json().then(function(data) {
        let optionHTML = '';
        optionHTML += "<option value='subcategory_all'>모두 선택" + "</option>";
        for (let subcategory of data) {
            optionHTML += "<option value='" + subcategory.subcategory + "'>" + subcategory.subcategory + "</option>";
        }
        subcategory_select.innerHTML = optionHTML;
        });
    });
}

//입력페이지 나이값 유효성 검사 함수
document.getElementById('input_age').onkeyup = function() {
    let input_age = document.getElementById('input_age');

    if (!check(input_age.value, /[0-9]/)) {
        document.getElementById('age_reg').style.display = "block";
    }
    else {
        document.getElementById('age_reg').style.display = "none";
    }
};

function check(val, re) {
    if(re.test(val)) {
        return true;
    }
    else {
        return false;
    }
}

//입력페이지 체중값 유효성 검사 함수
document.getElementById('input_weight').onkeyup = function() {
    let input_age = document.getElementById('input_weight');

    if (!check(input_age.value, /[0-9]/)) {
        document.getElementById('weigt_reg').style.display = "block";
    }
    else {
        document.getElementById('weigt_reg').style.display = "none";
    }
};

//입력페이지 submit 버튼 클릭했을 때 유효성 검사 후 에러를 alert하고 에러입력텍스트로 focus 하는 함수.
document.getElementById('input_page_button').onclick = function() {
    let input_age = document.getElementById('input_age');
    let input_weight = document.getElementById('input_weight')

    if (input_age.value=="") {
        alert("필수 사항 정보를 입력해주세요.");
        input_age.focus();
        return false;
    }
    else if (input_weight.value=="") {
        alert("필수 사항 정보를 입력해주세요.");
        input_weight.focus();
        return false;
    }

    if (input_age.value!="" & !check(input_age.value, /[0-9]/)) {
        alert("나이는 숫자만 입력 가능합니다.")
        input_age.focus();
        return false;
    }
    else if (input_weight.value!="" & !check(input_weight.value, /[0-9]/)) {
        alert("체중은 숫자만 입력 가능합니다.")
        input_weight.focus();
        return false;
    }
};