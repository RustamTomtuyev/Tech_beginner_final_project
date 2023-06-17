from flask import render_template,request,redirect, url_for,flash
from app import app
from models import *
from forms import contactform, Registerform,Login,message,favorit,search
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,current_user,logout_user

@app.route("/")
def main():
    data=Product.query.all()
    dataofproduct=category.query.all()



    return render_template("shop.html",data=data,data1=dataofproduct)

@app.route("/category/<int:id>")
def product(id):
    data=Product.query.filter_by(categoryid=id).all()
    dataofproduct=category.query.all()
    return render_template("shop.html",data=data,data1=dataofproduct)


@app.route("/product/<int:id>",methods=['GET','POST'])
def detail(id):
    data=Product.query.get(id)

    filterbycategory=Product.query.filter_by(categoryid=data.category.id).all()
    form=message()
    favform=favorit()
    if request.method == "POST":
        print(request.form)
        if form.validate_on_submit():
            
            form=message(request.form)
            if request.method == 'POST' and current_user.is_authenticated:
                review = Review(user_id=current_user.id, product_id=id, content=form.message.data)
                review.save()
        if favform.validate_on_submit():
            favform=favorit(request.form)
            if request.method == 'POST' and current_user.is_authenticated:
                favoriteee= Favorite(user_id=current_user.id, product_id=id, is_active=favform.is_active.data)
                favoriteee.save()


    listforshowing=[]
    review=Review.query.filter_by(product_id=id).all()
    for i in review:
        listforshowing.append([User.query.get(i.user_id).username,i.content])
    
    return render_template("detail.html",data=data,form=form,review=listforshowing,lenreview=review,favform=favform,filterbycategory=filterbycategory)

@app.route("/favorite",methods=['GET','POST'])
def favoritepage():

    if current_user.is_authenticated:
        productforuser=Favorite.query.filter_by(user_id=current_user.id).all()
        productt=[]
        for i in productforuser:
            if i.is_active==True:
                productt.append(Product.query.get(i.product_id))

   
    return render_template("favorites.html",data=productt)



@app.route('/favorites/delete/<int:id>', methods=['POST'])
def delete_favorite(id):
    if request.method == "POST" and current_user.is_authenticated:
        
        productforuser=Favorite.query.filter_by(user_id=current_user.id).all()
        print(productforuser)
        print(id)
        for i in productforuser:
            print(i.product_id)
            if i.product_id==id:
                i.is_active=False
                i.save()
                
                
    return redirect('/favorite')





@app.route("/contact",methods=['GET','POST'])
def contactt():
    form=contactform()
    if request.method == "POST":
        
        form=contactform(request.form)
        
        
        
        if form.validate_on_submit():
            
            dataa= contact(
                name=form.name.data,
                email=form.email.data,
                message=form.message.data,
                subject=form.subject.data,

            )
            dataa.save()
    
    return render_template("contact.html",form=form)


@app.route("/register/",methods=["GET","POST"])
def register():
    form=Registerform()
    
    if request.method=="POST":
        print("post")
        form=Registerform(request.form)

        if form.validate_on_submit():
            print("valid")
            listofname=User.query.filter_by(username=form.name.data).all()
            listofmail=User.query.filter_by(email=form.email.data).all()

            
            if len(listofname)>=1 and len(listofmail)>=1:
                flash('Name and Email already exists,error')
                return redirect('/register')
            elif len(listofname)>=1:
                flash('Please use another name, it exists,error')
                return redirect('/register')
            elif len(listofmail)>=1:
                flash('Please use another email, it exists,error')
                return redirect('/register')
            elif len(listofname)==0 and len(listofmail)==0:
                dataa= User(
                username=form.name.data,
                email=form.email.data,
                password=generate_password_hash(form.password.data)
                )
                dataa.save()
                flash('sign up successful!', )
                return redirect('/login')



            





    return render_template("register.html", form=form)





@app.route("/login",methods=["POST","GET"])
def login():
    form=Login()
    data=Product.query.all()
    if request.method=="POST":
        if form.validate_on_submit():
            user=User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password,form.password.data):
                login_user(user)
                x=user.username
                
                return render_template("shop.html",data=data,namee=x)



    
    return render_template("login.html",form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))



@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        products = Product.query.filter(Product.name.ilike(f'%{query}%')).all()

        return render_template('search.html', products=products, query=query)

