import Navlink from './Navlink'

function Header()
{

    const tabs = ["Home", "About Us", "Service", "Contact"]

    return(

        <div className="nav-container">
            <div className="nav-bar">
                <h1>Logo</h1>

                <div className="nav-links">
                    {
                        tabs.map((data, index) => (<Navlink key={index} name={data}/>))
                    }
                </div>
            </div>
        </div>

    )

}

export default Header;