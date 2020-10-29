function removeAll(subcategory) {
    for (var i=subcategory.options.length-1; i>=0; i--) {
        subcategory.remove(i);
    }
}

function insertOptions(category, subcategory) {
    var category = document.getElementById('category');
    var subcategory = document.getElementById('subcategory');

    selected_cate = category.options[category.selectedIndex].value;

    if (selected_cate != "category_init") {
        removeAll(subcategory);
        for (var i=1; i<=3; i++) {
            var opt = document.createElement('option');
            opt.value = selected_cate + i;
            opt.innerHTML = selected_cate + i;
            subcategory.options.add(opt);
        }
    }
    else {
        removeAll(subcategory);
        var opt = document.createElement('option');
        opt.value = "약품 분류(중분류)";
        opt.innerHTML = "약품 분류(중분류)";
        subcategory.options.add(opt);
    }
}