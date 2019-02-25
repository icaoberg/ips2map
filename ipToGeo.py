import ip2geotools
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myapplication')

def ipToGeo(filename):
	file = open(filename)
	locations = {}
	errorIPs = set()

	ip = file.readline().strip()
	while(ip):
		#print(ip)

		try: 
			response = DbIpCity.get(ip, api_key='free')
			#print(response)
			city = response.city
			region = response.region
			location = region + " " + city
			longitude = response.longitude
			latitude = response.latitude
			if location in locations:
				locations[location][2] += 1 # increase count
			else:
				if longitude == None or latitude == None:
					print("!!! Coordinates not found for",city,"from IP",ip)
					errorIPs.add((ip,"NoneLatLong"))
					alt = geolocator.geocode(region)
					longitude = alt.longitude
					latitude = alt.latitude
					print("Using coordinates for region",region,"instead.")
				locations[location] = [longitude, latitude, 1]
		except Exception as e:
			print("!!! Error",e,"occurred for IP address",ip,"skipping.")
			errorIPs.add((ip,e))
		'''
		except ip2geotools.errors.LocationError:
			print(ip + ':a generic location error.')
		except ip2geotools.errors.IpAddressNotFoundError:
			print(ip + ':the IP address was not found.')
		except ip2geotools.errors.PermissionRequiredError:
			print(ip + ':problem with authentication or authorization of the request; check your permission for accessing the service.')
		except ip2geotools.errors.InvalidRequestError:
			print(ip + ':invalid request.')
		except ip2geotools.errors.InvalidResponseError:
			print(ip + ':invalid response.')
		except ip2geotools.errors.ServiceError:
			print(ip + ':response from geolocation database is invalid (not accessible, etc.).')
		except ip2geotools.errors.LimitExceededError:
			print(ip + ':limits of geolocation database have been reached.')
		except:
			print(ip + ':key error.')
		'''
		
		ip = file.readline().strip()



	file.close()
	#print(locations)
	print("These IP addresses had errors:\n",errorIPs)
	return locations

