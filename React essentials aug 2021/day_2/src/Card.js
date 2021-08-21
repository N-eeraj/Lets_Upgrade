function Card(props)
{

    return(

        <div className="card">

            <img className="card-banner" src={props.img}></img>

            <h2 className="card-title">{props.title}</h2>
            <h4 className="card-sub">{props.sub}</h4>
            <p className="card-desc">{props.desc}</p>
            <button className="card-btn">Read More</button>

        </div>

    )

}

export default Card;