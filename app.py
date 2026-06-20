# ===== app.py（组长负责，请勿修改）=====
from flask import Flask, render_template, request, redirect, session

from data.site_info   import (SITE_NAME, SITE_SLOGAN,
                               NOTICE, CONTACT_TIP, FOOTER_TEXT)
from data.categories  import (CATEGORIES, CAMPUSES, CONDITION_OPTIONS)
from data.page_text   import (WELCOME_TEXT, SEARCH_HINT,
                               POST_HINT, RESULT_EMPTY,
                               POST_SUCCESS, LOGIN_TIP)
from data.listings    import LISTINGS
from data.users       import USERS

app = Flask(__name__)
app.secret_key = "dev-key-change-in-production"


# ── 首页：商品列表 + 筛选 ──────────────────────────────
@app.route("/", methods=["GET"])
def index():
    category = request.args.get("category", "")
    q        = request.args.get("q", "").strip().lower()

    items = LISTINGS
    if category:
        items = [i for i in items if i["category"] == category]
    if q:
        items = [i for i in items
                 if q in i["title"].lower()
                 or q in i["desc"].lower()]

    return render_template("index.html",
        site_name    = SITE_NAME,
        site_slogan  = SITE_SLOGAN,
        welcome_text = WELCOME_TEXT,
        search_hint  = SEARCH_HINT,
        notice       = NOTICE,
        footer_text  = FOOTER_TEXT,
        result_empty = RESULT_EMPTY,
        listings     = items,
        categories   = CATEGORIES,
        campuses     = CAMPUSES,
        cur_category = category,
        cur_q        = q,
        logged_in    = session.get("user"),
    )


# ── 商品详情页 ─────────────────────────────────────────
@app.route("/detail/<int:id>", methods=["GET"])
def detail(id):
    item = next((i for i in LISTINGS if i["id"] == id), None)
    if not item:
        return "商品不存在", 404
    return render_template("detail.html",
        item        = item,
        site_name   = SITE_NAME,
        contact_tip = CONTACT_TIP,
        footer_text = FOOTER_TEXT,
        logged_in   = session.get("user"),
    )


# ── 发布商品页（需要登录）─────────────────────────────
@app.route("/post", methods=["GET", "POST"])
def post():
    if not session.get("user"):
        return redirect("/login")
    if request.method == "POST":
        new_id = max((i["id"] for i in LISTINGS), default=0) + 1
        LISTINGS.append({
            "id":        new_id,
            "title":     request.form.get("title", ""),
            "category":  request.form.get("category", ""),
            "price":     int(request.form.get("price", "0") or "0"),
            "condition": request.form.get("condition", ""),
            "campus":    request.form.get("campus", ""),
            "seller":    session.get("user"),
            "desc":      request.form.get("desc", ""),
            "image":     request.form.get("image", ""),
        })
        return redirect("/")
    return render_template("post.html",
        site_name         = SITE_NAME,
        categories        = CATEGORIES,
        campuses          = CAMPUSES,
        condition_options = CONDITION_OPTIONS,
        post_hint         = POST_HINT,
        footer_text       = FOOTER_TEXT,
        logged_in         = session.get("user"),
    )


# ── 登录页 ────────────────────────────────────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if username in USERS and USERS[username] == password:
            session["user"] = username
            return redirect("/")
        else:
            error = "用户名或密码错误，请重试"
    return render_template("login.html",
        site_name   = SITE_NAME,
        site_slogan = SITE_SLOGAN,
        login_tip   = LOGIN_TIP,
        error       = error,
    )


# ── 退出登录 ──────────────────────────────────────────
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
